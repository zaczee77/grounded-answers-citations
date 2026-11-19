"""Grounded answers with citations, a small reference demo.

The demo answers questions only from the passages in a small invented
document set. Every claim in an answer carries a citation to the passage
it came from. A question the documents do not cover gets an honest
"I do not know" instead of a made up answer, and a question that is only
partly covered gets the covered part plus a note naming what is missing.

Plain Python, no external packages, no network calls.

Run it with: python3 demo/grounded_demo.py
"""

DOCUMENTS = [
    {
        "id": "DOC1",
        "title": "Northwind quarterly memo",
        "passages": [
            "Northwind revenue in the third quarter was 4.2 million dollars.",
            "Northwind opened 3 new stores in the third quarter, bringing the total to 41 stores.",
        ],
    },
    {
        "id": "DOC2",
        "title": "Northwind pricing sheet",
        "passages": [
            "The Standard plan price is 49 dollars per month.",
            "The Premium plan costs 99 dollars per month and includes priority support.",
        ],
    },
    {
        "id": "DOC3",
        "title": "Northwind returns policy",
        "passages": [
            "Refunds are accepted within 30 days of purchase.",
            "Refunds are returned to the original payment method.",
        ],
    },
    {
        "id": "DOC4",
        "title": "Northwind product meeting note",
        "passages": [
            "The loyalty feature launches in March.",
            "The loyalty feature gives one point for every dollar spent.",
        ],
    },
]

UNKNOWN = "I do not know based on the documents provided."


def find_passages(term):
    """Return every passage that contains the term, as (doc id, number, text)."""
    found = []
    for doc in DOCUMENTS:
        for number, text in enumerate(doc["passages"], start=1):
            if term.lower() in text.lower():
                found.append((doc["id"], number, text))
    return found


def answer(question, required_terms):
    """Answer a question from the documents, with a citation per claim.

    required_terms stands in for the term extraction a real system would
    do. A term is covered when at least one passage contains it. The
    answer covers only the covered terms, and names any term that is not
    covered, so nothing in the answer is ever ungrounded.
    """
    covered = {}
    missing = []
    for term in required_terms:
        passages = find_passages(term)
        if passages:
            covered[term] = passages[0]
        else:
            missing.append(term)

    if not covered:
        return {"question": question, "outcome": "not answered", "text": UNKNOWN}

    lines = []
    seen = set()
    for term in required_terms:
        if term in covered:
            doc_id, number, text = covered[term]
            if (doc_id, number) not in seen:
                seen.add((doc_id, number))
                lines.append(text + " [" + doc_id + ", passage " + str(number) + "]")

    if missing:
        lines.append(
            "The documents provided do not cover: " + ", ".join(missing) + "."
        )
        return {
            "question": question,
            "outcome": "partly answered",
            "text": " ".join(lines),
        }

    return {"question": question, "outcome": "answered", "text": " ".join(lines)}


def main():
    cases = [
        (
            "What was Northwind revenue in the third quarter?",
            ["revenue", "third quarter"],
        ),
        ("What is the price of the Standard plan?", ["Standard plan", "price"]),
        ("How many days is the refund window?", ["refund", "days"]),
        ("When does the loyalty feature launch?", ["loyalty", "launch"]),
        ("What is the churn rate for the Standard plan?", ["churn"]),
        (
            "What was Northwind revenue and what is the churn rate?",
            ["revenue", "churn"],
        ),
    ]

    results = [answer(question, terms) for question, terms in cases]

    for result in results:
        print("Question: " + result["question"])
        print("Outcome: " + result["outcome"])
        print("Answer: " + result["text"])
        print()

    answered = sum(1 for r in results if r["outcome"] == "answered")
    partly = sum(1 for r in results if r["outcome"] == "partly answered")
    not_answered = sum(1 for r in results if r["outcome"] == "not answered")
    print(
        str(len(results))
        + " questions asked, "
        + str(answered)
        + " answered, "
        + str(partly)
        + " partly answered, "
        + str(not_answered)
        + " not answered."
    )

    # Built in checks: every answered claim carries a citation, nothing is
    # answered without grounding, and no outcome is left undecided.
    assert len(results) == 6
    assert answered == 4
    assert partly == 1
    assert not_answered == 1
    for result in results:
        assert result["outcome"] in ("answered", "partly answered", "not answered")
        if result["outcome"] == "answered":
            assert "[" in result["text"] and "passage" in result["text"]
        if result["outcome"] == "not answered":
            assert result["text"] == UNKNOWN
        if result["outcome"] == "partly answered":
            assert "do not cover" in result["text"]
    print("All checks passed.")


if __name__ == "__main__":
    main()
