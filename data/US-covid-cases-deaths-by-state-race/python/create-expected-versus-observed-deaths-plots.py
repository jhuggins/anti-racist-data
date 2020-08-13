#
# Plot proportion of COVID deaths vs proportion of population that is black
#
# Author: Jonathan Huggins (huggins@bu.edu)
#

import os
import matplotlib
if 'DISPLAY' not in os.environ:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


import numpy as np
import pandas as pd
import seaborn as sns

def create_plot(group, df):
    # make scatter plot and best linear fit of
    # expected vs observed proportion of deaths
    deaths_col = 'Deaths_' + group + '_proportion'
    sns.lmplot(x=group, y=deaths_col, data=df)

    # plot x = y line
    max_prop = min(df[group].max(), df[deaths_col].max())
    l = mlines.Line2D([0, max_prop], [0, max_prop], linestyle=':', color='k')
    plt.gca().add_line(l)

    plt.title(group)
    plt.xlabel('Proportion of state population')
    plt.ylabel('Proportion of COVID deaths')

    plt.tight_layout()
    plt.savefig('expected-versus-observed-deaths-{}.png'.format(group.lower()))
    plt.close()


def main():
    # make figures pretty
    sns.set_style('white')
    sns.set_context('notebook', font_scale=1.5, rc={'lines.linewidth': 2})
    matplotlib.rcParams['legend.frameon'] = False

    # load dataset; exclude US
    df = pd.read_csv('US-covid-cases-deaths-population-by-state-race.csv',
                     index_col=0)
    df.drop('United States', inplace=True)
    df = df[pd.notnull(df.Deaths_Black_proportion)]

    for group in ['White', 'Black']:
        create_plot(group, df)


if __name__ == '__main__':
    main()
