#
# Combine state-level COVID death and case counts broken down by race with
# state-level population distributions by race. Also computes proportion
# of deaths and cases by race.
#
# Author: Jonathan Huggins (huggins@bu.edu)
#

import pandas as pd

state_abbreviations = {
  "AL": "Alabama",
  "AK": "Alaska",
  "AZ": "Arizona",
  "AR": "Arkansas",
  "CA": "California",
  "CO": "Colorado",
  "CT": "Connecticut",
  "DE": "Delaware",
  "DC": "District Of Columbia",
  "FL": "Florida",
  "GA": "Georgia",
  "HI": "Hawaii",
  "ID": "Idaho",
  "IL": "Illinois",
  "IN": "Indiana",
  "IA": "Iowa",
  "KS": "Kansas",
  "KY": "Kentucky",
  "LA": "Louisiana",
  "ME": "Maine",
  "MD": "Maryland",
  "MA": "Massachusetts",
  "MI": "Michigan",
  "MN": "Minnesota",
  "MS": "Mississippi",
  "MO": "Missouri",
  "MT": "Montana",
  "NE": "Nebraska",
  "NV": "Nevada",
  "NH": "New Hampshire",
  "NJ": "New Jersey",
  "NM": "New Mexico",
  "NY": "New York",
  "NC": "North Carolina",
  "ND": "North Dakota",
  "OH": "Ohio",
  "OK": "Oklahoma",
  "OR": "Oregon",
  "PA": "Pennsylvania",
  "RI": "Rhode Island",
  "SC": "South Carolina",
  "SD": "South Dakota",
  "TN": "Tennessee",
  "TX": "Texas",
  "UT": "Utah",
  "VT": "Vermont",
  "VA": "Virginia",
  "WA": "Washington",
  "WV": "West Virginia",
  "WI": "Wisconsin",
  "WY": "Wyoming"
}

def main():
    # load datasets
    covid_df = pd.read_csv('data/US-covid-cases-deaths-by-state-race.csv',
                           index_col=0)
    population_df = pd.read_csv('data/US-population-distribution-by-state.csv',
                                header=2, index_col=0)


    # translate covid_df to use full state names and add row with U.S. totals
    covid_df.index = covid_df.index.map(state_abbreviations)
    covid_df = covid_df[pd.notnull(covid_df.index)]
    covid_us = covid_df.sum(axis=0)
    covid_us.name = 'United States'
    covid_df = covid_df.append(covid_us)

    # clean up population data frame
    del population_df['Footnotes']
    del population_df['Total']
    population_df.replace('<.01', 0, inplace=True)

    # add covid proportions to data frame
    for col in covid_df.columns:
        typ, grp = col.split('_', 1)
        if grp != 'Total':
            covid_df[col + '_proportion'] = covid_df[col] / covid_df[typ + '_Total']

    # construct merged dataframe and write to disk
    df = population_df.join(covid_df, how='inner')
    df.to_csv('data/US-covid-cases-deaths-population-by-state-race.csv',
              index_label='Location')


if __name__ == '__main__':
    main()
