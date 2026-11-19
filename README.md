# Grounded answers with citations

A reference pattern and a small runnable demo for answering questions only from documents that are actually in front of the system, with a citation attached to every claim. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

A language model asked a question about a document will answer even when the document says nothing about it. The answer sounds certain, cites nothing, and cannot be checked. A person reading it has no way to tell which parts came from the document and which parts the model supplied on its own. In a deal workspace, a prior authorization file, or a billing review, that gap is the whole risk. An unchecked claim can move a decision that a real document would not support.

A citation is the fix, but only when the citation is real. A citation that points at a passage which does not contain the claim is decoration. The pattern here is simple: a claim may appear in an answer only when a passage containing it has been found first, and the citation names that passage.

## What the pattern does

1. The question is broken into the terms an answer would need to be grounded in. The demo stands in for that extraction step with a short list of required terms per question.
2. Every required term is looked up in the document set. A term is covered when at least one passage contains it.
3. The answer is built only from covered terms. Each claim is the passage text itself, followed by a citation naming the document and the passage number.
4. A term no passage covers is named as missing, in the answer itself. A partly covered question gets a partly answered answer, never a complete sounding one.
5. A question with no covered term at all is not answered. The system says it does not know based on the documents provided. That sentence is a feature, not a failure.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It answers six questions against four invented documents: a quarterly memo, a pricing sheet, a returns policy, and a product meeting note. Four questions are answered with a citation each, one question about a churn rate the documents never mention is not answered, and one question that mixes a covered revenue term with an uncovered churn term is answered only for the revenue part, with the missing term named.

The docs folder describes the pattern in full: the lookup step, the three outcomes, and the rule that a citation must name a passage that actually contains the claim.

## What this is not

This demo is not the Txvni product. It models the cited question answering pattern Txvni uses, at miniature scale, with invented sample data. No real documents, deals, or model outputs appear here, and no accuracy, retrieval, or outcome number is claimed. A real system would replace the term lookup with real retrieval over real ingested documents, and would add the steps this demo does not model, such as ranking passages, resolving conflicting passages, and checking the answer against the cited text. None of those are modeled here.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
