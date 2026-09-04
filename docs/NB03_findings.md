# Notebook 03 — the paper stands, and the hypothesis does not

3 September 2026

## Send this to the editor

Every published claim survives the panel repair.

| Measure | Published 2016→2025 | Repaired | HAC *p* |
|---|---|---|---|
| Hill α | 1.4908 → 1.1413 | 1.4669 → 1.1413 | 0.0062 |
| Gini | 0.5856 → 0.7186 | 0.5879 → 0.7186 | <0.0001 |
| top 1% | 0.1132 → 0.3005 | 0.1097 → 0.3005 | <0.0001 |
| top 10% | 0.4807 → 0.6376 | 0.4822 → 0.6376 | <0.0001 |
| HHI | 0.0089 → 0.0234 | 0.0087 → 0.0234 | <0.0001 |

2016 endpoints move by at most 0.004, 2025 values are identical, coverage rises from 391
firms to 403. `editor_robustness_table.csv` is ready to attach.

## H1 fails, and the failure is the interesting part

**The test instrument was wrong.** Splitting firms into bit-intensity quartiles and running
a Hill estimator inside each gave 1.26, 1.86, 1.12, 1.90 across four *ordered* groups. That
is not a weak gradient, it is noise — the top decile of a middle quartile is not a tail of
anything, and Hill on a slice estimates nothing. Retired.

**The index ranks the wrong firms.** Top of the 2025 list: Incyte, Marriott, Synopsys,
AbbVie, Regeneron, Molson Coors, VICI Properties. **Amazon is in the bottom quartile.**
Microsoft is Q2; Apple, Alphabet and Nvidia are Q3. Across every year the ten largest firms
scatter 2–5 into each of the four quartiles.

Gross margin and asset lightness pick out pharmaceuticals, franchising and long-lease REITs.
They do not pick out the firms *Machine, Platform, Crowd* is about.

**But the index is not useless, and the pattern in where it works is the finding.** Bit
intensity separates the top 5%, 10% and 25% of index value from the rest at *p* < 0.0001,
and is flat at the top 1% (difference 0.02, *p* = 0.74). It predicts being *near* the top
and is silent about who is *at* it. The extreme tail — the part the Pareto index measures,
and therefore the part the first paper's result is about — is exactly where the measure
stops working.

## Why: the tail has gone physical

Microsoft's asset lightness falls from 0.905 to 0.608 across the decade. Alphabet 0.796 →
0.620. Amazon 0.651 → 0.564. Nvidia goes the other way, 0.947 → 0.950, because it is
fabless — the fabs belong to TSMC.

Grouping firms as *tail* (ever in the top 1%), *digital* (GICS digital, non-tail) and
*rest*, on the current incomplete data:

| Group | asset lightness 2016 → 2025 | slope/yr | *p* |
|---|---|---|---|
| **tail** | 0.848 → **0.664** | **−0.0142** | <0.0001 |
| digital | 0.870 → 0.902 | +0.0035 | <0.0001 |
| rest | 0.748 → 0.776 | +0.0037 | <0.0001 |

The top of the index is becoming capital-intensive **while every other group becomes
lighter**, and it crosses from above the digital average to well below it. Gross margin for
the tail is flat over the same years, so this is not a margin story — it is specifically
capital.

That is the JRFM Future Scope prediction, measured: the binding constraint moves from
software, which is non-rival and free to copy, to compute, which is rival and physical.

## What notebook 04 does

**Cell 3 first, because the claim is not yet safe.** Amazon is missing PP&E in six years of
ten, Meta in six, Alphabet in five — the exact firms the capital story rests on. Notebook
01's frames-first shortcut left holes precisely there. Cell 3 runs full companyfacts for the
120 largest firms and adds **capital expenditure**, which measures the compute build-out
directly instead of by inference from the balance sheet.

Then: two index specifications side by side, with and without asset lightness — because if
the most bit-intensive firms are now the most capital-intensive, that component has the
wrong sign for the mechanism it was chosen to proxy.

Then H1 with instruments that can detect what it claims: a membership model for the top
*k*%, and a **Gabaix–Ibragimov rank regression** that puts both groups in one equation so
the difference in tail exponent is a single coefficient with a single *p*-value.

Then H3 (Gibrat) and H4 (persistence), neither of which notebook 03 reached.

## Preview, on the incomplete data

- H1 membership: coefficients rise monotonically with *k* and vanish at 1% — 5% *p* = 0.024,
  10% *p* = 0.003, 25% *p* < 0.0001, 1% *p* = 0.95.
- Gabaix–Ibragimov on the specification without asset lightness: high-bit-intensity firms
  have a **thinner** tail, difference +0.18, *p* = 0.011. H1 rejected, and in the opposite
  direction.
- Gibrat: growth on size +0.0072, *p* = 0.12. Not rejected at the mean.
- Only **Apple and Microsoft** are in the top 1% in all ten years. Shorrocks mobility 0.50.

If that holds, the paper's claim is that concentration at the top of the index is not
explained by the economics of bits — and that the firms occupying that tail have spent the
decade acquiring exactly the kind of rival, physical capital those economics were defined
against. It is a negative result with a mechanism, which is worth more than a confirmation
would have been.
