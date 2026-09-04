# Notebook 07 — the out-of-sample test half-worked, and it caught two errors

3 September 2026

## The thirty-year test did its job

It confirmed one half of the hypothesis and refused the other, which is what an
out-of-sample test is for.

| Layer | 1996–2015 slope | *p* | 2016–2025 slope | *p* |
|---|---|---|---|---|
| **fabricates compute** | **−0.186 pp/yr** | **0.0015** | −0.080 | <0.0001 |
| designs compute | −0.037 | 0.079 | +1.354 | <0.0001 |
| operates compute | +0.113 | 0.31 | +1.466 | <0.0001 |

The decline of the firms that own fabs is a **thirty-year structural trend**, significant
two decades before the window this paper measures. Intel went from 5.19% of the top hundred
firms by value to 0.38%; Texas Instruments from 0.54% to 0.34%. That half is confirmed.

The rise of the firms that design without fabs is **not**. Before 2016 it was flat or
slightly falling. The entire rise is 2016–2025, and mostly 2020–2025. The paper can date it
but cannot call it structural.

The corrected taxonomy — one rule, who owns the fab — separates cleanly: designs 0.028 capex
and 0.944 asset lightness against fabricates 0.138 and 0.761.

## But notebook 07 had two errors, and both change quoted numbers

**It used the unrepaired panel.** Meta is absent 2016–2021 and appears to arrive from
nothing. On the repaired panel Meta is 1.64% of index value in 2016, so *operates compute*
gains **+9.78 points, not +11.17**.

**And firm identity was by ticker, so Alphabet split in two** — GOOGL +6.18 and GOOG −2.90,
because the panel keeps whichever class was larger each year. Its real contribution is
+3.28.

## The attribution, which is what I should have run first

| Firm | 2016 | 2025 | contribution |
|---|---|---|---|
| **NVDA** | 0.31% | 7.40% | **+7.10** |
| GOOGL | 2.90% | 6.18% | +3.28 |
| MSFT | 2.60% | 5.86% | +3.27 |
| AAPL | 3.32% | 6.58% | +3.26 |
| TSLA | 0.00% | 2.44% | +2.44 |
| AVGO | 0.40% | 2.68% | +2.28 |
| AMZN | 1.91% | 4.02% | +2.11 |

Across the whole index the gains are not absurdly concentrated — Herfindahl 0.060, about
**16.6 effective firms**, with the top five taking 47%. But *within* the design layer they
are:

| | 2016 | 2025 | change | trend |
|---|---|---|---|---|
| designs compute | 1.23% | 11.50% | +10.27 | +1.062 pp/yr |
| **without Nvidia** | 0.92% | 4.10% | **+3.18** | +0.331 pp/yr, *p* < 0.0001 |
| without Nvidia and Broadcom | 0.52% | 1.42% | +0.91 | +0.111 pp/yr, *p* < 0.0001 |

Nvidia is 69% of the design layer's gain. The *trend* survives dropping it — still highly
significant — but the magnitude collapses by two-thirds.

**The operating layer is the robust one.** Its largest member, Alphabet, is only 34% of the
gain, and dropping it still leaves +6.51 points. No single firm carries it.

## The boundary cases matter more than I expected

Apple owns no fab and designs its own silicon, so the rule as written makes it a designer —
and it contributed +3.26, more than the design layer without Nvidia. Tesla is the same
argument with less force. Reported under all three treatments:

| Layer | Apple/Tesla as other digital | Apple as designer | Both as designers |
|---|---|---|---|
| designs compute | +10.28 | +13.54 | +15.98 |
| **operates compute** | **+9.79** | **+9.79** | **+9.79** |

The operating result is invariant. The design result swings from +0.91 (dropping two firms)
to +15.98 (adding two) — a range the paper must report rather than a point estimate it
chooses.

## What the paper can now say

1. **Concentration rose steeply and robustly** — the JRFM claims survive the panel repair.
2. **It is not explained by the economics of bits.** Bit intensity from accounting predicts
   the top 25% but not the top 1%, and within sectors high-bit-intensity firms have
   *thinner* tails (+0.299, *p* = 0.0002).
3. **The firms running compute became capital-intensive**, and it is those firms
   specifically — hyperscalers against other tail firms +0.0139 (*p* = 0.0003), tail against
   everyone else *p* = 0.27.
4. **Capital did not buy share.** The bridge is negative.
5. **Value went to the design layer** — but 69% of that is Nvidia, and the paper says so in
   the sentence that reports it.
6. **The fabricator decline is structural**, confirmed across thirty years.

That is a complete argument with its own limits marked. Notebook 08 is the last one: it runs
in about a minute, has no downloads, and every cell is already verified against your
notebook 07 output — the numbers above are what it will produce. After that I send a draft.
