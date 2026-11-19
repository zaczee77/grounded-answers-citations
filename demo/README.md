# Demo: grounded answers with citations

A small reference demo of the cited question answering pattern behind Txvni: a question is answered only from passages found in the document set, every claim carries a citation naming its document and passage, and a question the documents do not cover is not answered.

## How to run it

From the repository root, or from this folder:

```
python3 demo/grounded_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. Question 1. What was Northwind revenue in the third quarter. Answered, with a citation to the quarterly memo, passage 1.
2. Question 2. What is the price of the Standard plan. Answered, with a citation to the pricing sheet, passage 1.
3. Question 3. How many days is the refund window. Answered, with a citation to the returns policy, passage 1.
4. Question 4. When does the loyalty feature launch. Answered, with a citation to the product meeting note, passage 1.
5. Question 5. What is the churn rate for the Standard plan. Not answered. No passage mentions churn, so the answer says it does not know based on the documents provided.
6. Question 6. What was Northwind revenue and what is the churn rate. Partly answered. The revenue part is answered with its citation, and the answer names churn as a term the documents do not cover.

## What it printed when it was tested

6 questions asked, 4 answered, 1 partly answered, 1 not answered. The built in checks passed: every answered claim carries a citation, nothing is answered without grounding, and no outcome is left undecided.

## What the sample data is

Every document title, passage, company name, amount, price, and date in `grounded_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real price, or a real model output. A real system would run its lookup against real ingested documents. None of those are modeled here.

## Files

1. `grounded_demo.py`: the demo. The document set, the term lookup, the three outcomes, and the built in assertions.
2. `README.md`: this file.
