# Notebook 05 — the mechanism holds, and the paper's frame has to narrow

3 September 2026

## The result survives every test I could put to it

**The leases objection is answered.** Capex is a cash-flow measure ASC 842 cannot touch;
the two independent measures correlate at −0.774; the decline survives on plain-tag
firm-years at −0.0073 (*p* < 0.0001); and the 2019 step is **positive** (+0.026), because
right-of-use assets inflate total assets. Lease accounting *masks* the decline rather than
manufacturing it.

**The CIK repair mattered.** With Exxon on its real CIK (34088) across all ten years rather
than entering in 2025 alone at 0.333, the tail's asset-lightness slope falls from −0.0190 to
−0.0112. Notebook 04's number was inflated by composition, exactly as suspected. The
corrected slope is still *p* < 0.0001, and it is now identical on the balanced panel
(−0.0120), so it is not composition any more.

**The H1 inversion is robust.** Ranking firms only against their own sector makes it
stronger: +0.299 (*p* = 0.0002) against +0.215 raw. High-bit-intensity firms have thinner
tails within their own industries. Not pharmaceuticals.

## But the frame has to narrow, in two ways

**One: it is the hyperscalers, not "the tail".** The difference-in-differences with firm
fixed effects is unambiguous:

| Contrast | capex extra trend | *p* |
|---|---|---|
| hyperscaler vs other tail firms | **+0.0139** | **0.0003** |
| hyperscaler vs everyone else | +0.0102 | 0.0043 |
| tail vs everyone else | +0.0038 | 0.27 |

"Large firms became capital-intensive" is not true. *Four firms that operate compute* became
capital-intensive. Widening the tail confirms it: asset lightness at the top 1% is −0.0112
(*p* < 0.0001), at the top 5% −0.0008 (*p* = 0.36), at the top 10% +0.0007 (*p* = 0.27).

**Two: it is not only the AI years.** Through 2023 alone the hyperscaler capex slope is
+0.0053 (*p* < 0.0001) and asset lightness −0.0216 (*p* < 0.0001). Only 24% of the level
change happened by 2023, so AI accelerated it sharply — but the reallocation was underway,
and the paper is not describing two years.

## The bridge failed, and that is the finding

The two halves of the paper needed connecting: concentration rose, and the top became
capital-intensive. If capital spending predicted gains in value share, one argument. It does
not — the panel coefficient is **−0.115** (*p* = 0.067) and the cross-sectional one −0.435
(*p* = 0.19). Both negative. What predicts share gain is being digital (+0.560, *p* = 0.0001).

The firms that gained most over the decade are AMD (+2.54 log points), Broadcom (+1.90),
Micron (+1.40), KLA (+1.37), Lam Research (+1.34), Arista (+1.27), Cadence (+0.97),
Synopsys (+0.95). Semiconductors, semiconductor equipment and EDA — **mean capital intensity
around 0.03**. These firms *sell* compute. The hyperscalers, who buy it, tripled their
capital intensity and did not lead the share gains. Nvidia is the limiting case: fabless,
capex 0.028, asset lightness 0.944 and rising, and it became the largest firm in the index.

## Where that leads — the layer result

I added a cell to notebook 06 rather than send you back for another round. Splitting the
digital economy by position in the compute stack:

| Layer | firms | share of index 2016 → 2025 | gain | mean capex |
|---|---|---|---|---|
| **designs compute** | 10 | 1.7% → 11.8% | **+10.07 pts** | 0.040 |
| **operates compute** | 5 | 9.9% → 19.7% | **+9.79 pts** | 0.158 |
| fabricates compute | 8 | 2.0% → 2.2% | +0.25 pts | 0.124 |
| other digital | 36 | 13.8% → 12.4% | −1.39 pts | 0.066 |
| not digital | 331 | — | large loss | 0.101 |

Designers and operators together went from 11.6% to 31.5% of index value — which is
essentially the whole concentration result. And design capex intensity *fell* over the
decade, 0.071 → 0.036, while operating capex tripled.

**The economics of bits did not end. They moved up one layer.** The non-rival, IP-heavy,
near-zero-marginal-cost economics chapter 6 describes now sit with the firms whose product
is a design rather than a machine — and those firms captured as much value as the
capital-intensive operators, on a quarter of the capital. The layer that owns the physical
bottleneck, fabrication, captured almost nothing.

That maps directly onto Acemoglu: what determines who captures the surplus from a general
purpose technology is position in the stack, not the properties of the technology.

**One caveat that must appear in the paper.** The layer classification was written *after*
seeing the cross-section. It is a hypothesis this data generated, not one it tested, and it
is labelled that way in the notebook. Confirmation needs out-of-sample evidence — other
indices, or the years after this sample.

## Is the empirical work done?

After notebook 06 runs, yes. It has no downloads and takes under five minutes. If the
divergence coefficient holds, the bridge stays negative, and the trend survives through
2023 — all three of which the dry run already shows on your notebook 05 data — the next
thing I send you is a draft rather than a notebook.
