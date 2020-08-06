# U.S. state-level cumulative COVID cases and deaths by race

## Overview

Data on the number of COVID cases and deaths by race and ethnicity for each
U.S. state and Washington D.C.
Recent data on the racial/ethnic make-up of each state is included as well
for comparison.

## Description

The original COVID data is [here](US-covid-cases-deaths-by-state-race.csv)
and the population-level data is [here](US-population-distribution-by-state.csv).
The two sources are combined using [this script](generate-US-covid-cases-deaths-population-by-state-race.py),
with the output [here](US-covid-cases-deaths-population-by-state-race.csv).

## Example Analysis 

This [python script](create-expected-versus-observed-deaths-plots.py) was used
to compare the expected proportion of COVID deaths (based on the population) with the
observed proportion of deaths.
While further adjustments would be ideal (for example, to account for age composition effects),
the available data suggest a disproportionate affect on the black community.

![Expected vs Observed Deaths (White)](expected-versus-observed-deaths-white.png)

![Expected vs Observed Deaths (Black)](expected-versus-observed-deaths-black.png)

## Sources and Licenses

Sources: <a href="https://covidtracking.com/">The COVID Tracking Project</a>
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This data is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>

<a href="https://www.kff.org/other/state-indicator/distribution-by-raceethnicity/">Kaiser Family Foundation: Population Distribution by Race/Ethnicity (2018)</a>
