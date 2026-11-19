# The grounded answers pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description says it ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. Cited question answering is the load bearing part of that list. A deal team asks about a document, and the answer has to be traceable back to the document, or it is not usable.

This pattern writes down the cited answering step Txvni uses, so it can be reused wherever an answer meets a decision that matters. The guardrail pattern from the companion repository is the automated gate that checks an output before it is used. This pattern is the gate that comes before it: it decides what the answer is allowed to contain in the first place.

## The pipeline

A question enters, the required terms are pulled out of it, each term is looked up in the document set, and the answer is built only from the terms that were found. An answer leaves with exactly one outcome: answered, partly answered, or not answered. That single rule is what turns a set of passages into a grounded answer.

Each claim in the answer is the passage text itself, followed by a citation that names the document and the passage number. A claim without a citation cannot appear, because there is no step that creates a claim except copying a found passage. A missing term is named in the answer, so the reader sees exactly what the documents did not cover.

## The three outcomes

The lookup decides the outcome, and only the lookup does.

1. Answered. Every required term was found in at least one passage. The answer is the found passages, each with its citation. The reader can check every claim by opening the cited passage.
2. Partly answered. Some terms were found and some were not. The answer covers only the found terms, each with its citation, and then names the terms the documents do not cover. The answer is honest about its own edge.
3. Not answered. No required term was found. The answer is a single sentence saying the system does not know based on the documents provided. There is no partial answer to give, because there is nothing to ground it in.

The order matters. The lookup runs before any answer text exists. An answer is never written first and cited afterwards, because a citation added after the fact can point at a passage that does not support the claim. Grounding first, wording second.

## Design principles

1. A claim without a citation does not exist. If no passage contains it, it does not go in the answer, whatever the question asked.
2. The citation names the passage, not the document. A document level citation lets a wrong claim hide inside a long document. A passage level citation can be checked in seconds.
3. A missing term is named, not hidden. An answer that quietly drops the part it could not cover reads as a complete answer. An answer that names the gap reads as what it is.
4. Not knowing is a normal outcome. A system that never says it does not know is not answering from documents. It is guessing, and dressing the guess as an answer.
5. The same passage is cited once. When two terms resolve to the same passage, the claim appears once, not twice. Repetition is not extra evidence.
6. Retrieval and wording are separate steps. The lookup decides what may be said. The wording only assembles what the lookup found. The model never supplies a fact the lookup did not find.

## What the demo shows, and what it does not show

The demo in this repository shows the pattern at miniature scale: four invented documents, eight invented passages, six questions, and three outcomes. It shows the shape of the work: a lookup, a citation per claim, one outcome per question, and a named gap where the documents run out. It does not show real documents, real retrieval, real deal work, or measured results, and it does not show the Txvni product. Real retrieval, real passage ranking, real handling of conflicting passages, and real verification of an answer against its cited text are all real parts of a grounded answering system, and none of them are modeled in the demo. The demo is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
