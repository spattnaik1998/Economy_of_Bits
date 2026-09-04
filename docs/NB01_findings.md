# Notebook 01 — what the audit found

3 September 2026

Notebook 01 was written to answer one question before any modelling effort was spent:
does the data exist at the coverage the design needs? It answered that, and it also
turned up something that matters more — a defect in the panel underneath the JRFM paper
that is currently under review.

---

## 1. The good news first

**EDGAR works, and it works well.** 4,325 of 4,443 market-cap firm-years matched to a
filer — a 97.3% match rate, with **zero unmatched tickers**. Revenue is present for 97.3%
of firm-years and total assets for 99.3%. The frames-plus-companyfacts design does what it
was meant to do.

**Gate 2 passed decisively.** The correlation between provisional bit intensity and the
GICS digital label is **+0.194**. That is the single most important number in this run.
It says bit intensity is a genuinely different variable from the sector split, not a
relabelling of it — which is the entire justification for writing the companion paper.
Had it come back at 0.9, the paper would have been renaming a variable rather than
explaining one.

**BEA is fully reachable**, so H5 survives. Census BTOS is not in the API, so AI-adoption
becomes discussion context rather than a tested hypothesis.

---

## 2. Gate 1 failed at 56%, and the reason is mostly not a bug

The binding constraint is cost of goods sold, at 62.0%. Coverage by sector:

| Sector | COGS | PP&E | all four | firm-years |
|---|---:|---:|---:|---:|
| Financials | 15.3% | 77.2% | 13.9% | 606 |
| Utilities | 23.7% | 82.9% | 19.5% | 287 |
| Real Estate | 34.5% | 42.7% | 25.5% | 255 |
| Communication Services | 35.7% | 85.7% | 27.8% | 126 |
| Energy | 52.2% | 74.7% | 37.1% | 178 |
| Industrials | 66.0% | 86.5% | 58.3% | 652 |
| Consumer Discretionary | 67.0% | 92.3% | 63.5% | 403 |
| Health Care | 83.5% | 92.8% | 77.7% | 502 |
| Information Technology | 89.9% | 94.2% | 84.4% | 514 |
| Consumer Staples | 96.8% | 86.5% | 85.3% | 312 |
| Materials | 88.7% | 95.1% | 86.3% | 204 |

Banks and insurers do not report cost of goods sold because they have no goods. Utilities
and REITs likewise. That is roughly a quarter of the index for which **gross margin is
undefined as a matter of accounting, not missing as a matter of data.** No amount of extra
downloading fixes it, and hypothesis (b) — my cell-7 fallback bug — is not the binding
constraint.

Two real tag gaps do exist and are worth fixing: REITs report
`RealEstateInvestmentPropertyNet` rather than `PropertyPlantAndEquipmentNet` (hence 42.7%),
and a handful of large filers drop `PropertyPlantAndEquipmentNet` in later years.

**Consequence for the design.** Gross margin cannot be a required component. The index has
to be rebuilt on components with near-universal coverage — asset lightness, intangible
share of assets, R&D intensity — with gross margin as a robustness check on the subsample
where it is defined. R&D needs care: a blank is ambiguous between "spent nothing" and "did
not report", and filling zeros would push every non-R&D firm to one point and manufacture
the separation H1 is supposed to test.

---

## 3. The finding that matters: the panel loses firms when their ticker changes

Roster coverage in the JRFM panel rises monotonically:

| Year | 2016 | 2018 | 2020 | 2022 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|
| % of roster in panel | 80.8 | 83.9 | 88.0 | 93.2 | 96.0 | 97.0 |

The paper reads this as survivorship — delisted firms lose their price history at Yahoo.
That is true for part of it. But a large share is something else: **firms that were in the
index the entire decade, are alive today, and are absent from the early panel purely
because their ticker changed.** Yahoo is keyed on current tickers, so a historical ticker
returns nothing, and the firm enters the panel only in the year it was renamed.

| Company | Old ticker | Years in panel | Actually in the index |
|---|---|---|---|
| **Meta Platforms** | FB → META | **2022–2025** | continuously since 2013 |
| Elevance Health | ANTM → ELV | 2022–2025 | continuously |
| Warner Bros. Discovery | DISCA → WBD | 2022–2025 | continuously |
| Ball Corp | BLL → BALL | 2022–2025 | continuously |
| Cencora | ABC → COR | 2023–2025 | continuously |
| Everest Group | RE → EG | 2023–2025 | continuously |
| Revvity | PKI → RVTY | 2024–2025 | continuously |
| Healthpeak | PEAK → DOC | 2024–2025 | continuously |
| Truist | STI → TFC | 2019–2025 | continuously |
| **Fiserv** | FISV → FI | **2016–2022, then gone** | continuously |

Fiserv runs the other way and is the cleanest proof it is a naming artefact rather than a
corporate one: it is present until 2022 and vanishes in 2023, the year it renamed to FI —
while remaining in the index throughout.

### Why this threatens the headline result

Meta is the problem case. It is one of the largest firms in the index and a core member of
the digital group, and it is **absent from the 2016–2021 cross-sections and present from
2022**. The digital group's tail index is reported as falling 1.381 → 0.640, and the sharp
part of that fall begins in 2023. A firm of Meta's size joining the group mid-sample
mechanically changes the tail it is estimated from.

The aggregate series shows the same shape: `alpha_hill` sits between 1.41 and 1.63 from
2016 through 2022, then drops to 1.26, 1.20, 1.14. The panel gains 24 firms in 2022 alone.

This does **not** mean the result is wrong. NVIDIA's 2023–2025 rise is real and large, and
the direction of the bias is genuinely ambiguous: missing mid-cap firms in 2016 would
*raise* measured concentration, while missing Meta would *lower* it. Which dominates has to
be computed, not asserted. But the composition of the panel changes systematically across
exactly the window the trend is estimated over, and a referee will find it.

---

## 4. What notebook 02 should do

**Repair the panel before building anything on top of it.** The bit-intensity index can
wait a week; a defect in the paper under review cannot.

1. **Build a ticker-alias map from EDGAR.** `data.sec.gov/submissions/CIK##########.json`
   carries `formerNames` and the filer's ticker history. Every roster ticker resolves to a
   CIK, and every CIK resolves to its *current* ticker. Fetch prices under the current
   ticker, then attribute them to the historical roster entry.
2. **Re-derive market caps** for the recovered firms, applying the same split adjustment
   and plausibility screen, and re-run the JRFM estimates.
3. **Report the movement.** If the headline numbers hold, the paper gains a robustness
   check and the coverage limitation shrinks. If they move, we tell the editor before a
   referee tells us.
4. **Separate the two channels explicitly.** Renamed-but-alive firms are recoverable and
   should be recovered. Acquired firms — Activision, Cerner, Citrix, Ansys, Hess, Discover
   — genuinely stop trading, and that residual is honest survivorship the paper reports.
5. Only then: rebuild bit intensity on the coverage this audit actually found, add the
   REIT and PP&E fallback tags, and finish the platform coding from the review queue.

One thing to check on the way: Marsh & McLennan has no price history at all despite being
continuously listed and never renamed. I predicted a per-ticker retry would recover it in
the first paper's run and it did not. That one is a Yahoo failure rather than a naming
issue, and it needs a second source or an explicit exclusion.
