<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-falsifiability

**How could this evidence be shown wrong?**

Ranks oversight evidence by independent falsifiability.

## Problem

Self-reported success counts as evidence. Ranks evidence by how it could be shown wrong; self-report never alone.

## Install

```
pip install loomground-falsifiability
```

## Usage

```python
from loomground_falsifiability import Evidence, Falsifiability, support_verdict
support_verdict([Evidence("run#7", Falsifiability.SELF_REPORT), Evidence("trace#12", Falsifiability.OBSERVED_TOOL_CALL)])
support_verdict([Evidence("run#7", Falsifiability.SELF_REPORT)])
```

## Example

```
in : self-report + observed tool call / self-report only
out: Verdict.SATISFIED
     Verdict.OPEN
```

## Interface

- rank, ascending: `SELF_REPORT < DECLARED_PLAN < OBSERVED_TOOL_CALL < VERIFIED_OUTCOME < SPAN_GROUNDED < REPLAYABLE`
- `SUPPORT_FLOOR = DECLARED_PLAN`, raisable via `floor=`
- `support_verdict(evidence, floor=) → Verdict`: `SATISFIED` at or above floor, else `OPEN`
- `best_support(evidence)` · `fold_support(claims, floor=) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `issue_aggregation.aggregate_issues`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-falsifiability`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 16 tests · Python >=3.10 · solver 0.5

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
