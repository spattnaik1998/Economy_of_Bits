#!/usr/bin/env python3
"""Render the analysis results as LaTeX tables.

    python scripts/make_tables.py

Reads  results/<stage>/<file>.csv
Writes build/tables/tab_*.tex

Each table is emitted as a bare `tabular` environment with booktabs rules and no
caption, so it can be \\input into any document that supplies its own float,
caption and label. `build/` is a generated directory and is git-ignored.

The formatting rules are shared rather than repeated per table:
  * p-values print to four decimals, and as $<$0.0001 below that;
  * coefficients that can be either sign print with an explicit sign;
  * `&`, `%` and `_` are escaped anywhere a value comes from a data field.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
TABLES = ROOT / "build" / "tables"

LAYER_NAMES = {
    "operates compute": "Operates",
    "designs compute": "Designs",
    "fabricates compute": "Fabricates",
    "compute equipment": "Equipment",
    "other digital": "Other digital",
    "not digital": "Not digital",
}


# ------------------------------------------------------------------ helpers
def esc(value) -> str:
    """Escape the LaTeX specials that occur in these data fields."""
    return str(value).replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def pval(v) -> str:
    if pd.isna(v):
        return "---"
    return r"$<$0.0001" if v < 0.0001 else f"{v:.4f}"


def layer(name: str) -> str:
    return LAYER_NAMES.get(name, str(name).capitalize())


def read(stage: str, name: str) -> pd.DataFrame:
    return pd.read_csv(RESULTS / stage / f"{name}.csv")


def write(name: str, body: str) -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    (TABLES / f"{name}.tex").write_text(body, encoding="utf-8")
    print(f"  wrote build/tables/{name}.tex")


def tabular(colspec: str, header: str, rows: list[str], preamble: str = "") -> str:
    return (
        f"\\begin{{tabular}}{{{colspec}}}\n\\toprule\n"
        + preamble
        + header
        + "\n\\midrule\n"
        + "\n".join(rows)
        + "\n\\bottomrule\n\\end{tabular}\n"
    )


# ------------------------------------------------------------------- tables
def tab_coverage() -> None:
    """Index coverage before and after the rename repair."""
    d = read("nb03_index", "coverage_final")
    rows = [
        f"{int(r.year)} & {int(r.roster)} & {int(r.published_n)} & {int(r.final_n)} "
        f"& {r.pct_published:.1f} & {r.pct_final:.1f} \\\\"
        for r in d.itertuples()
    ]
    write("tab_coverage", tabular(
        "rrrrrr",
        r"Year & Roster & Published $n$ & Repaired $n$ & Published \% & Repaired \% \\",
        rows))


def tab_layers() -> None:
    """Membership of the four layers of the compute stack."""
    layers = json.loads((RESULTS / "nb07_stack" / "run_summary.json").read_text())["layers"]
    rows = [
        f"{layer(k)} & \\texttt{{{esc(', '.join(sorted(layers[k])))}}} \\\\[4pt]"
        for k in ("operates compute", "designs compute",
                  "fabricates compute", "compute equipment")
        if k in layers
    ]
    write("tab_layers", tabular(
        "@{}p{2.3cm}p{10.4cm}@{}",
        r"Layer & Constituent firms \\",
        rows))


def tab_repaired() -> None:
    """Concentration measures as published and after repair."""
    labels = {"alpha_hill": r"Hill tail index $\alpha$", "gini": "Gini coefficient",
              "top1_share": r"Top 1\% share", "top10_share": r"Top 10\% share",
              "hhi": "HHI"}
    d = read("nb03_index", "editor_robustness_table")
    rows = [
        f"{labels[r.measure]} & {r.published_2016:.4f} & {r.published_2025:.4f} "
        f"& {r.final_2016:.4f} & {r.final_2025:.4f} & {r.final_slope:+.5f} "
        f"& {pval(r.final_p_hac)} \\\\"
        for r in d.itertuples()
    ]
    write("tab_repaired", tabular(
        "@{}lrrrrrr@{}",
        r"Measure & 2016 & 2025 & 2016 & 2025 & Slope/yr & $p$ (HAC) \\",
        rows,
        preamble=(r" & \multicolumn{2}{c}{As published} & \multicolumn{2}{c}{After repair}"
                  " & & \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n")))


def tab_top1() -> None:
    """Membership of the top one per cent by year."""
    d = read("nb07_stack", "top1_membership_by_year")
    rows = [
        f"{int(r.year)} & {int(r.n)} & {r.share_pct:.1f} & \\texttt{{{esc(r.firms)}}} \\\\"
        for r in d.itertuples()
    ]
    write("tab_top1", tabular(
        "@{}rrrp{7.2cm}@{}",
        r"Year & Firms & Share (\%) & Members \\",
        rows))


def tab_h1() -> None:
    """Linear probability models of tail membership on bit intensity."""
    d = read("nb04_mechanism", "h1_tail_membership")
    d = d[d.spec == "BI_B"]
    rows = [
        f"Top {esc(r.top_pct)} & {int(r.n_top)} & {r.mean_BI_in_top:.3f} "
        f"& {r.mean_BI_rest:.3f} & {r.coef:+.4f} & {r.t:.2f} & {pval(r.p)} \\\\"
        for r in d.itertuples()
    ]
    write("tab_h1", tabular(
        "lrrrrrr",
        r"Tail & Firm-years & Mean $B$ in tail & Mean $B$ rest & Coefficient & $t$ & $p$ \\",
        rows))


def tab_gi() -> None:
    """Gabaix-Ibragimov rank regressions across bit-intensity groups."""
    d = read("nb04_mechanism", "h1_gabaix_ibragimov")
    rows = []
    for r in d.itertuples():
        spec = "Four-component" if r.spec == "BI_A" else "Three-component"
        rows.append(
            f"{spec} & Top {esc(r.tail_frac)} & {int(r.n)} & {r.alpha_low_BI:.4f} "
            f"& {r.alpha_high_BI:.4f} & {r.difference:+.4f} & {pval(r.p_difference)} \\\\")
    write("tab_gi", tabular(
        "llrrrrr",
        r"Index & Tail & $n$ & $\hat\alpha$ low $B$ & $\hat\alpha$ high $B$ "
        r"& Difference & $p$ \\",
        rows))


def tab_did() -> None:
    """Difference-in-differences estimates of divergence."""
    d = read("nb06_bridge", "did_divergence")
    d = d[d.variable.isin(["capex_intensity", "asset_light"])]
    rows, previous = [], None
    for r in d.itertuples():
        name = "Capital intensity" if r.variable == "capex_intensity" else "Asset lightness"
        if previous is not None and name != previous:
            rows.append(r"\addlinespace")
        rows.append(
            f"{name if name != previous else ''} & {esc(r.contrast)} & {int(r.n)} "
            f"& {r.extra_trend:+.5f} & {r.t_stat:.2f} & {pval(r.p)} \\\\")
        previous = name
    write("tab_did", tabular(
        "@{}llrrrr@{}",
        r"Measure & Contrast & $n$ & Extra trend & $t$ & $p$ \\",
        rows))


def tab_lease() -> None:
    """Asset lightness as reported and excluding lease right-of-use assets."""
    d = read("nb09_long_capital", "lease_adjusted_asset_lightness")
    d = d[d.year >= 2016]
    rows = [
        f"{int(r.year)} & {r.asset_light:.4f} & {r.asset_light_ex_lease:.4f} "
        f"& {r.rou_share:.4f} \\\\"
        for r in d.itertuples()
    ]
    write("tab_lease", tabular(
        "rrrr",
        r"Year & As reported & Excluding lease assets & Lease assets / assets \\",
        rows))


def tab_windows() -> None:
    """Capital intensity by group, split at 2016."""
    d = read("nb09_long_capital", "capex_trends_three_windows")
    d = d[~d.window.astype(str).str.startswith("2008-2025")]
    rows, previous = [], None
    for r in d.sort_values(["group", "window"]).itertuples():
        name = str(r.group).capitalize()
        window = "2008--2015" if str(r.window).startswith("2008-2015") else "2016--2025"
        if previous is not None and name != previous:
            rows.append(r"\addlinespace")
        rows.append(
            f"{name if name != previous else ''} & {window} & {r.first:.3f} "
            f"& {r.last:.3f} & {r.slope:+.5f} & {pval(r.p)} \\\\")
        previous = name
    write("tab_windows", tabular(
        "@{}llrrrr@{}",
        r"Group & Window & First & Last & Slope/yr & $p$ \\",
        rows))


def tab_benchmark() -> None:
    """Hyperscaler capital intensity against sector benchmarks."""
    d = read("nb09_long_capital", "capital_intensity_benchmark")
    d = d[d.year.isin([2008, 2012, 2015, 2018, 2021, 2025])]
    rows = []
    for _, r in d.iterrows():
        it, ut = r["Information Technology"], r["Utilities"]
        distance = 100 * (r["hyperscalers"] - it) / (ut - it)
        rows.append(
            f"{int(r.year)} & {r['hyperscalers']:.3f} & {it:.3f} "
            f"& {r['Real Estate']:.3f} & {ut:.3f} & {distance:.0f}\\% \\\\")
    write("tab_benchmark", tabular(
        "rrrrrr",
        r"Year & Hyperscalers & IT sector & Real estate & Utilities & Distance \\",
        rows))


def tab_intel() -> None:
    """Intel: capital intensity against share of index value."""
    d = read("nb09_long_capital", "intel_case")
    rows = [
        f"{int(r.year)} & {r.capex_intensity:.3f} & {r.share_of_index_pct:.3f} \\\\"
        for r in d.itertuples()
    ]
    write("tab_intel", tabular(
        "rrr",
        r"Year & Capital intensity & Share of index (\%) \\",
        rows))


def tab_decomposition() -> None:
    """Change in index value shares by layer, 2016-2025."""
    d = read("nb08_attribution", "decomposition_repaired").sort_values(
        "change_pp", ascending=False)
    rows = [
        f"{layer(r.layer)} & {r.share_2016:.2f} & {r.share_2025:.2f} & {r.change_pp:+.2f} \\\\"
        for r in d.itertuples()
    ]
    write("tab_decomposition", tabular(
        "@{}lrrr@{}",
        r"Layer & Share 2016 (\%) & Share 2025 (\%) & Change (pp) \\",
        rows))


def tab_loo() -> None:
    """Leave-one-out attribution by layer."""
    d = read("nb08_attribution", "leave_one_out_by_layer")
    rows = [
        f"{layer(r.layer)} & {int(r.n_firms)} & {r.total_pp:+.2f} "
        f"& \\texttt{{{r.largest}}} & {100 * r.share_from_largest:.0f}\\% "
        f"& {r.ex_largest_pp:+.2f} \\\\"
        for r in d.itertuples()
    ]
    write("tab_loo", tabular(
        "@{}lrrlrr@{}",
        r"Layer & Firms & Total (pp) & Largest & Its share & Excluding it \\",
        rows))


def tab_sensitivity() -> None:
    """Sensitivity of the decomposition to the Apple and Tesla placements."""
    d = read("nb08_attribution", "classification_sensitivity")
    treatments = list(d.treatment.unique())
    pivot = d.pivot(index="layer", columns="treatment", values="change_pp")
    order = ["designs compute", "operates compute", "fabricates compute",
             "compute equipment", "other digital", "not digital"]
    rows = [
        f"{layer(name)} & " + " & ".join(f"{pivot.loc[name, t]:+.2f}" for t in treatments)
        + r" \\"
        for name in order if name in pivot.index
    ]
    write("tab_sensitivity", tabular(
        "@{}l" + "r" * len(treatments) + "@{}",
        "Layer & " + " & ".join(esc(t) for t in treatments) + r" \\",
        rows))


def tab_30y() -> None:
    """Layer shares of top-100 US market value over thirty years."""
    d = read("nb07_stack", "layer_share_trends_30y")
    rows, previous = [], None
    for r in d.itertuples():
        if previous is not None and r.layer != previous:
            rows.append(r"\addlinespace")
        rows.append(
            f"{layer(r.layer) if r.layer != previous else ''} "
            f"& {esc(str(r.window).replace('-', '--'))} & {r.first:.2f} & {r.last:.2f} "
            f"& {r.slope_pp_per_year:+.3f} & {pval(r.p)} \\\\")
        previous = r.layer
    write("tab_30y", tabular(
        "@{}llrrrr@{}",
        r"Layer & Window & First & Last & Slope (pp/yr) & $p$ \\",
        rows))


BUILDERS = [tab_coverage, tab_layers, tab_repaired, tab_top1, tab_h1, tab_gi,
            tab_did, tab_lease, tab_windows, tab_benchmark, tab_intel,
            tab_decomposition, tab_loo, tab_sensitivity, tab_30y]


def main() -> None:
    print(f"reading  {RESULTS}")
    print(f"writing  {TABLES}")
    for build in BUILDERS:
        build()
    print(f"{len(BUILDERS)} tables regenerated.")


if __name__ == "__main__":
    main()
