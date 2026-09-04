# Notebook 08 — and why there is one more after all

3 September 2026

## Do I have what I need? Almost — I missed something in my own data

Notebook 08 did what it was meant to. The attribution is clean, the leave-one-out is
decisive, and `paper_facts.csv` collects every number in one place.

But in checking whether anything was outstanding I looked at the EDGAR facts we already
downloaded and found they **reach back to 2007**. Every notebook so far has filtered them to
2016–2025 out of habit, throwing away nine years that were already on disk. That is my
error, not a new requirement, and it changes three things enough to be worth one more run.

## What notebook 08 settled

**The gains are moderately concentrated at index level** — Herfindahl 0.060, about 16.6
effective firms, top five taking 47%. Nvidia alone is 17% of all gains.

| Firm | contribution |
|---|---|
| NVDA | +7.10 |
| GOOGL | +3.28 |
| MSFT | +3.27 |
| AAPL | +3.26 |
| TSLA | +2.44 |
| AVGO | +2.28 |
| AMZN | +2.11 |

**But within layers the picture splits.** The operating layer is a genuine category: its
largest member is 34% of the gain and dropping Alphabet still leaves +6.51 points. The
design layer is Nvidia — 69% of it, and dropping Nvidia takes +10.28 to +3.18. The trend
survives (+0.331 pp/yr, *p* < 0.0001) but the magnitude collapses by two-thirds.

**Classification sensitivity confirms it.** Under three treatments of Apple and Tesla, the
operating result is +9.79 every time; the design result runs +10.28 / +13.54 / +15.98. The
paper reports a range for one and a point estimate for the other.

## What the extra nine years change

**When the build-out started.** This is the most useful thing in the whole project, and the
ten-year window hid it:

| Group | 2008–2015 slope | *p* | 2016–2025 slope | *p* |
|---|---|---|---|---|
| hyperscaler | **+0.0041** | **0.0022** | +0.0146 | <0.0001 |
| designs | −0.0074 | 0.010 | −0.0016 | <0.0001 |
| fabricates | +0.0011 | 0.60 | +0.0062 | <0.0001 |
| rest of index | +0.0027 | <0.0001 | +0.0005 | 0.013 |

The hyperscaler build-out was **already significant before the paper's window**, running at
about a quarter of its later rate. It is a cloud-era reallocation that AI accelerated
3.5-fold — not an AI-era event. The design layer has been shedding capital for eighteen
years, 0.107 → 0.022. The fabricators' burden, by contrast, is genuinely recent: flat to
2015, rising sharply after.

**How far it has gone.** Stated as a position on a spectrum rather than an adjective:

| | hyperscalers | IT sector | utilities | distance travelled |
|---|---|---|---|---|
| 2008 | 0.053 | 0.057 | 0.167 | −3% |
| 2015 | 0.067 | 0.053 | 0.264 | 7% |
| 2020 | 0.131 | 0.050 | 0.339 | 28% |
| 2025 | 0.277 | 0.059 | 0.398 | **64%** |

Two-thirds of the way from a software cost structure to a regulated-infrastructure one, in
seventeen years. Not past it — the paper should not call them utilities.

**Intel, which is the argument in one firm.** Capital intensity 0.138 (2008) → 0.475 (2023),
outspending every hyperscaler, while its share of index value went 0.908% → 0.165% in 2024.
The spending peaked exactly as the share bottomed. Nvidia over the same years spent almost
nothing on plant and became the largest firm in the index. The paper does not need to claim
the fab *caused* Intel's decline — execution and process failures are the larger story — but
the capital commitment and the value capture went in opposite directions, and that is what
the bit-economics account does not predict.

## Two data problems the run also caught

**Revenue is mis-tagged for some filers.** Charter shows revenue of $1.1bn against $9.4bn of
capital spending; its real revenue is about $55bn. American Tower, Crown Castle, Extra Space
and Healthpeak show the same. This inflated the Real Estate sector benchmark to 0.505 —
after cleaning it is **0.271**, and Communication Services falls from 0.148 to 0.093. Had I
used the uncleaned figure the calibration above would have been wrong.

**Oracle at 0.826 was a fiscal-year artefact**, as suspected — it closes in May, and the row
labelled 2025 is a period ending May 2026. 361 firm-years are now excluded on two rules:
revenue below half the firm's own median, or capital spending exceeding revenue.

**And the lease question is closed with a number.** Hyperscaler asset lightness excluding
operating-lease right-of-use assets is 0.7883 against 0.7890 as reported. The difference is
seven ten-thousandths, and the decline visibly begins in 2010–2012, years before ASC 842.
One sentence in the paper instead of a defensive paragraph.

## This one really is the last

Notebook 09 has no downloads and takes about two minutes; every cell is verified against
your notebook 08 output, so the numbers above are what it will produce. After that I have
what I need and the next thing I send is a draft.
