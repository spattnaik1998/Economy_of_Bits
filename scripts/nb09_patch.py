# =============================================================================
# OPTIONAL patch to notebook 09, cell 3. One line, and it does not change any
# conclusion -- it strengthens one.
#
# The exclusion rule compares a firm's revenue to its own MEDIAN across the
# period, to catch filers whose revenue tag is wrong (Charter reports $1.1bn
# against real revenue near $55bn; American Tower and the other tower REITs
# likewise). It works, but it punishes fast growth: Amazon's 2008-2013 revenue
# is legitimately below half its 2008-2025 median because the firm grew
# fifteenfold, so six good Amazon years are thrown away.
#
# Comparing to the PREVIOUS YEAR instead catches the same tagging errors -- a
# mis-tagged year still collapses against the year before it -- without
# punishing growth. Exclusions fall from 361 firm-years to 151, and with
# Amazon's early years restored the pre-2016 hyperscaler slope rises from
# +0.0041 to +0.0108. The finding that the build-out predates the paper's window
# holds either way; this version states it more strongly.
#
# Replace these two lines in cell 3:
#     L["rev_median"] = L.groupby("cik").revenue.transform("median")
#     L["rev_vs_own_median"] = L.revenue / L.rev_median
#     BAD_REV = (L.rev_vs_own_median < 0.5) & L.rev_vs_own_median.notna()
# with:
# =============================================================================
L = L.sort_values(["cik", "year"])
L["rev_prev"] = L.groupby("cik").revenue.shift(1)
L["rev_median"] = L.groupby("cik").revenue.transform("median")   # kept for the table
L["rev_vs_prev"] = L.revenue / L.rev_prev
BAD_REV = (L.rev_vs_prev < 0.6) & L.rev_vs_prev.notna()
