# Errata and corrected defects

Every substantive bug found in our own work during this project, what it did to the
numbers, and how it was fixed. Recorded because several of these moved published results,
and because a reader checking the code should know where the traps were.

Defects are listed in the order they were found. Those marked **published** affected the
companion JRFM paper; the rest were caught before any number left the pipeline.

---

## Panel construction

### Ticker renames dropped the largest firms from the earliest years — **published**

A constituent roster records the ticker under which a firm was a member. A price query on
a retired ticker returns nothing, so Facebook (`FB` → `META`), Anthem (`ANTM` → `ELV`),
SunTrust (`STI` → `TFC`) and sixteen others vanished from the cross-section in exactly the
years in which they were largest. Coverage was 80.8% of the roster in 2016 against 97.0%
in 2025, so the loss was concentrated at the start of the sample — the worst place for it
in a trend estimate.

*Fix:* a curated nineteen-entry alias table carrying EDGAR filing evidence for each swap
(`results/nb03_index/alias_table_curated.csv`), plus a collision guard that refuses an
alias which would place two tickers on the same firm in the same year. Recovers 74
firm-years and lifts 2016 coverage to 83.3%. Every trend verdict holds; the 2016 levels
move by at most 0.0035, in the conservative direction.

### The automatic rename detector produced garbage

The first attempt at the above was a rule: a filer with `formerNames` in its EDGAR
submission history whose price series predates the swap. Nearly every long-lived
registrant has `formerNames`, so the rule fired almost everywhere and produced pairings
including `CELG` → `NOW`, `ALXN` → `MRNA`, `FRC` → `AXON`, `INFO` → `MOH` and
`TWTR` → `ACGL`. Of 175 firm-years recovered, 101 were spurious, and the false ones moved
the concentration series *further* than the true ones did.

*Fix:* the rule was abandoned rather than tuned. Raw candidates are retained in
`results/nb02_panel_repair/` for inspection.

### Two CIK mismappings

A ticker-to-CIK lookup returned CIK `2115436` for `XOM` — a 2025 re-registration carrying
a single year of filings — instead of the operating entity, CIK `34088`. `BLK` was mapped
to `2012383` instead of `1364742`.

*Fix:* a rule flagging any match whose filing history is shorter than the firm's presence
in the index, plus an explicit override table.

### GOOG and GOOGL were treated as two firms

Keying firm identity on ticker split Alphabet into two series contributing +6.18 and
−2.90 percentage points to the decomposition, instead of one firm contributing +3.28.

*Fix:* firm identity is keyed on SEC CIK throughout.

### Notebook 07 ran on the unrepaired panel

Meta was absent 2016–2021, inflating the "operates compute" layer's gain from +9.78 to
+11.17 percentage points. The layer-share figures emitted by notebook 07 still plot the
unrepaired series and should be regenerated before reuse.

*Fix:* notebook 08 recomputes the decomposition on the repaired panel; the corrected
values are in `results/nb08_attribution/decomposition_repaired.csv`.

---

## Measurement

### Intangibles included goodwill

`IntangibleAssetsNet` as commonly tagged includes goodwill, which measures acquisitiveness
rather than knowledge capital. In this panel goodwill share loads *negatively* on the
first principal component of the bit-intensity variables, pulling against R&D.

*Fix:* only `IntangibleAssetsNetExcludingGoodwill` is used.

### Sector vocabulary leak

Yahoo's sector labels ("Healthcare", "Consumer Cyclical") sat beside GICS labels
("Health Care", "Consumer Discretionary") in the same column, so sector-neutral
standardisation was computed within inconsistent groups.

*Fix:* a `YF_TO_GICS` mapping applied before any grouping.

### Pooling raw market caps across years

Index total capitalisation roughly triples over the window, so a pooled sample of raw caps
is a mixture of ten differently scaled distributions and is not Pareto by construction.

*Fix:* within-year normalised capitalisation share is used for all pooled estimation.

### Revenue mis-tagging inflated the real-estate benchmark

Charter Communications reported $1.1bn of revenue against $9.4bn of capital expenditure
(actual revenue ≈ $55bn); several tower REITs showed the same pattern. This lifted the
Real Estate capital-intensity benchmark for 2025 to 0.505.

*Fix:* a screen dropping firm-years whose revenue falls below one fifth of the previous
year's. The cleaned benchmark is 0.271. Oracle's 0.826 in one year was a separate
artefact of its May fiscal year-end, fixed by mapping fiscal years to the calendar year
holding the majority of the period.

### The exclusion screen punished fast growth — our own defect

The first version of the screen above compared revenue to the firm's *own median* across
the panel, which drops the early years of any firm that grows quickly. It removed Amazon
for 2008–2013, a period over which Amazon grew fifteenfold.

*Fix:* compare to the previous year instead. Exclusions fall from 361 firm-years to 151,
and the pre-2016 hyperscaler capex slope strengthens from +0.0041 to +0.0108. The looser
screen moves the result in the finding's favour, which is why it is flagged here.

---

## Estimation

### The quartile-Hill test was the wrong instrument

Splitting firms into quartiles of bit intensity and estimating a Hill index within each
returned 1.26, 1.86, 1.12, 1.90 across four *ordered* groups. The Hill estimator applied
to the top decile of a middle quartile is not estimating a tail at all.

*Fix:* retired and replaced by a tail-membership linear probability model and the
Gabaix–Ibragimov rank regression, in which the difference between groups is a single
coefficient with a single *p*-value.

### Density versus survival tail exponents — **published**

The `powerlaw` package returns the **density** exponent, *p(x) ~ x^−α*; the Hill estimator
targets the **survival** exponent, *P(X > x) ~ x^−α*. They differ by exactly one. Reporting
them side by side without converting compares two different quantities.

*Fix:* both are reported on the survival convention, and the conversion is asserted in the
companion repository's test suite.

### `powerlaw` silently caps the exponent — **published**

`powerlaw` 2.0 constrains the density exponent through
`DEFAULT_PARAMETER_RANGES = {'alpha': [0, 3]}`, so it cannot return a survival α above 2.
On synthetic data with a true α of 2.5 it returns exactly 2.000 and warns about nothing.

*Fix:* the unbounded analytic MLE is computed at the package's own `xmin` and an
`at_parameter_bound` flag is set when the two disagree. No estimate in this project is
near the bound, but code reused elsewhere may be.

### A magnitude understated in an early summary

An early summary described the reported-versus-ex-lease asset-lightness gap as "seven
ten-thousandths", taking the 2017 value alone. Across the series the gap widens to 2.6
percentage points by 2025 (0.5841 reported against 0.5579 ex-lease). The direction still
favours the finding; the magnitude was understated.

---

## Environment and tooling

| Symptom | Cause | Fix |
|---|---|---|
| `TypeError: float() argument must be... not 'Response'` | Cell 9 stored a correlation in `r`; cell 12 reused `r` for a `requests.Response` | Recompute the gate inline; never reuse single-letter names across cells |
| `TypeError: unsupported operand for -: 'method' and 'method'` | Columns named `first`/`last` collide with pandas `Series.first`/`.last`. Our sandbox ran pandas 3.0, where the methods are removed, so the dry run passed while Colab (pandas 2.x) failed | Renamed to `first_value`/`last_value`, bracket access throughout |
| `fillna` rejected an ndarray | `F.layer.fillna(np.where(...))` is not supported | Mask and assign: `_u = F.layer.isna(); F.loc[_u, "layer"] = np.where(...)` |
| Parquet write failed on `paper_facts` | Mixed `str`/`float` in the `value` column | `.astype(str)` before writing |
| Census BTOS probe returned 404 | The path was guessed; BTOS is not in the API catalogue at all | Replaced with a catalogue search; the series was dropped |
| API probes reported false failures | The `companyfacts` check looked for `us-gaap` in the first 4000 characters, and Apple's `dei` block is longer than that | Search the whole body, or check for `"facts"` |
