# Notebook 06 — the argument is complete; one notebook left

3 September 2026

## The three results

**Divergence.** Hyperscalers against other tail firms, capex extra trend **+0.0139,
*p* = 0.0003**, with firm fixed effects. Against everyone else, +0.0102 (*p* = 0.0043). But
**tail against everyone else is +0.0038, *p* = 0.27**. It is not large firms. It is the
firms that operate compute. Widening the tail confirms it: asset lightness is −0.0112 at
the top 1%, −0.0008 at 5% (*p* = 0.36), +0.0007 at 10% (*p* = 0.27).

**Not just the AI years.** Through 2023 alone the hyperscaler capex slope is +0.0053
(*p* < 0.0001) and asset lightness −0.0216 (*p* < 0.0001). Only a quarter of the level change
had happened by then, so AI accelerated it sharply — but the reallocation was underway.

**The bridge is negative.** Capital spending does not predict gains in value share: −0.115
(*p* = 0.067) in the panel, −0.435 (*p* = 0.19) in the cross-section. What predicts share gain
is being digital (+0.560, *p* = 0.0001).

## The layer result

| Layer | share 2016 → 2025 | gain | mean capex | vs non-digital |
|---|---|---|---|---|
| designs compute | 1.7% → 11.8% | **+10.07 pts** | 0.040 | *t* = 3.34, *p* = 0.009 |
| operates compute | 9.9% → 19.7% | **+9.79 pts** | 0.158 | *t* = 8.54, *p* = 0.0006 |
| fabricates compute | 2.0% → 2.2% | +0.25 pts | 0.124 | *t* = 3.20, *p* = 0.015 |
| other digital | 13.8% → 12.4% | −1.39 pts | 0.066 | *p* = 0.14 |

Three layers, three directions, all at *p* < 0.0001: designers' capex **fell** 0.071 → 0.032
while operators' rose 0.093 → 0.387 and fabricators' rose 0.100 → 0.154.

## Why one more notebook

**The classification is wrong at the edges.** Analog Devices, NXP, Skyworks and Qorvo are in
"designs compute" and all four own fabs. Their capital intensity (0.053–0.083) is double the
true fabless group's (0.010–0.039). Replacing sector intuition with one rule — *who owns the
fab* — gives a clean separation: designs 0.028 capex and 0.944 asset lightness against
fabricates 0.138 and 0.761.

**And the layer story was formed on the data it was tested on.** The panel runs to 1996, and
the two decades before the AI build-out informed nothing. I ran that test here, and it
**half confirms and half disconfirms** — which is exactly why it was worth running:

| Layer | 1996–2015 slope | *p* | 2016–2025 slope | *p* |
|---|---|---|---|---|
| fabricates compute | **−0.186** | **0.0015** | −0.080 | <0.0001 |
| designs compute | −0.037 | 0.079 | +1.354 | <0.0001 |
| operates compute | +0.113 | 0.31 | +1.466 | <0.0001 |

The **fabricator decline is a thirty-year structural trend**, significant long before the
window this paper measures. Intel went from 5.19% of the top hundred firms by value to
0.38%. That half is confirmed out of sample.

The **designer rise is not**. Before 2016 it was flat or slightly falling; the entire rise
is 2016–2025 and mostly 2020–2025. The paper must say that the value migration to the design
layer is a recent phenomenon it can date but cannot yet call structural.

## The decomposition — where the first paper's 18.7 points came from

| Layer | 2016 | 2025 | change |
|---|---|---|---|
| operates compute | 8.53% | 19.69% | **+11.17 pts** |
| designs compute | 1.27% | 11.50% | **+10.24 pts** |
| other digital | 13.79% | 18.23% | +4.44 |
| compute equipment | 0.36% | 1.00% | +0.64 |
| fabricates compute | 1.81% | 1.55% | **−0.25** |
| not digital | 74.26% | 48.02% | −26.23 |

Two layers supplied 21.4 of the 26.2 points that non-digital firms lost. And the top 1%
itself: Apple, Alphabet, Microsoft and Berkshire in 2016; **Nvidia, Apple, Alphabet,
Microsoft and Amazon in 2025, with Nvidia first**. Berkshire and Tesla passed through.

The JRFM paper's headline and this paper's mechanism are the same event at two resolutions.

## Value per unit of capital

| Layer | median share gain | mean capex | gain per capex point |
|---|---|---|---|
| designs compute | +1.27 | 0.028 | **45.3** |
| compute equipment | +1.34 | 0.031 | 43.1 |
| operates compute | +0.62 | 0.164 | 3.8 |
| fabricates compute | −0.33 | 0.148 | −2.2 |

Descriptive, not causal — it says how the decade turned out, not what would have happened
had a firm chosen otherwise. The paper must say so in those words.

## After notebook 07

The empirical work is done and the next thing I send is a draft. Notebook 07 has no
downloads and runs in about two minutes; I have already executed every cell against your
notebook 06 output, so the numbers above are what it will produce.
