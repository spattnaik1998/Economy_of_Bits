# Notebook 02 — what the repair found, and what it broke

3 September 2026

## The headline: the JRFM paper survives

Re-estimating on a panel with the verified renames applied:

| Measure | Published 2016→2025 | Repaired 2016→2025 | HAC *p* |
|---|---|---|---|
| Hill α | 1.4908 → 1.1413 | **1.4669 → 1.1413** | 0.0062 |
| Gini | 0.5856 → 0.7186 | **0.5879 → 0.7186** | <0.0001 |
| top 1% share | 0.1132 → 0.3005 | **0.1097 → 0.3005** | <0.0001 |
| top 10% share | 0.4807 → 0.6376 | **0.4822 → 0.6376** | <0.0001 |

The 2016 endpoints move by at most 0.004 and the 2025 values are unchanged. The α trend
comes back at *p* = 0.0062 against a published 0.006. Coverage in 2016 rises from 391 firms
to 403.

Adding Meta to 2016–2021 *lowers* early concentration slightly, exactly as predicted, and
the effect is far too small to threaten the trend. **The defect is real and immaterial.**
That is worth sending the editor unprompted: the paper now has a robustness check against
a criticism a referee could otherwise have raised.

## The part that went wrong

Notebook 02's automatic alias detector was bad, and it is worth being precise about why.

The rule was: EDGAR records a former name for this filer, **and** its filing history
predates the index swap. Nearly every long-lived filer has a `formerNames` entry — Skyworks,
Molina and Moderna all do, usually from a routine legal-name tidy-up years earlier — and
every established firm added to the index has filings predating the day it joined. So the
test passed for almost everyone, and produced:

```
CELG → NOW      Celgene's slot filled with ServiceNow
ALXN → MRNA     Alexion's with Moderna
FRC  → AXON     First Republic's with Axon
INFO → MOH      IHS Markit's with Molina
TWTR → ACGL     Twitter's with Arch Capital
```

**101 of 175 recovered firm-years came from false aliases**, about 1.6% of panel market
value. They moved the estimates more than the true aliases did — the contaminated run gave
α 1.417 → 1.090 and a Gini of 0.600 → 0.732, both visibly different from the clean numbers
above. Had I trusted the detector, the "repair" would have been a second defect.

The lesson is narrow and worth writing down: *a test that almost everything passes is not
a test.* Date proximity would have worked — Anthem's name change is recorded 4 days from
the ticker swap, Everest's 5 days, Torchmark's 6 — while the false pairs sit 3 to 18 years
away. But pure ticker changes with no name change (BLL→BALL, FISV→FI, PEAK→DOC) have no
date to be close to, so no automatic rule covers the whole set.

**Notebook 03 replaces the detector with a curated table of 19 renames, each carrying its
EDGAR evidence in a column a referee can check without running anything.**

## What notebook 03 does

**Section A** re-runs the repair cleanly and produces the editor-facing robustness table.

**Section B** is the companion paper's actual measurement. Bit intensity from four
components — asset lightness, intangible share, R&D intensity, gross margin — z-scored
within year, requiring at least two components per firm-year, which covers 88% of the panel
and 90% of its market value.

Three fixes went in after dry-running it here:

1. **Intangibles now exclude goodwill.** Goodwill is the premium paid in an acquisition, so
   goodwill/assets measures acquisitiveness, not bit-ness. With it included the component
   loaded *negatively* on the first principal component, pulling against the other three.
2. **Sector vocabulary harmonised.** Notebook 02's Yahoo fallback leaked non-GICS labels, so
   "Healthcare" sat beside "Health Care" and "Consumer Cyclical" beside "Consumer
   Discretionary" — splitting sectors in every table and hiding firms from the digital flag.
3. **Pooled tail estimates now use within-year normalised capitalisation.** The index total
   triples over the decade, so pooling raw caps across years is a mixture of differently
   scaled distributions and is not Pareto even when every year is. The tail index is
   scale-invariant, so dividing by the year's total removes the scale without touching the
   shape.

## One thing to brace for

On the dry run, **H1 does not survive inside the GICS partition** and H2 shows nothing.
Splitting non-digital firms into high and low bit intensity gives tail indices of 1.83 and
1.87 — a difference of 0.04 in the wrong direction, *p* = 0.85. Platform against pipeline
within a bit-intensity quartile is likewise insignificant.

That dry run used a partly reconstructed panel and predates the pooling fix, so it is a
warning rather than a result. But it is the plausible outcome, and it is worth deciding now
what the paper says if it holds: that the concentration in digital firms is **not** explained
by measurable bit intensity or by two-sidedness, which would be a real finding and an
uncomfortable one for chapter 6's account. The honest paper reports that. It would also
point at the remaining candidate — that what concentrates value is not the cost structure
but the *installed base*, which no accounting statement records.

Bit intensity is also correlated with GICS digital at only +0.20, so the two partitions
genuinely differ. If neither predicts the tail, that is informative about both.
