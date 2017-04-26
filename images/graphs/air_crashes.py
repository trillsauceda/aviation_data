import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('ggplot')

a_df = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv')

a_df['Years'] = pd.to_datetime(a_df['Date']).map(lambda x:x.year)

def get_deaths_per_year(df):
    fatal_years = df.groupby([df['Years']])['Fatalities'].sum()
    years = fatal_years.index
    counts = fatal_years.values

    fig,ax = plt.subplots(figsize=(15,6))
    ind = np.arange(len(years))
    ax.bar(ind, counts)

    plt.title('Annual Fatalities by Airplane',fontsize=20)
    plt.xlabel('Years')
    plt.ylabel('# of Deaths')
    plt.xticks(ind, years)
    plt.setp(ax.get_xticklabels(),rotation='vertical')
    plt.show()

def get_deaths_per_year_2(df):
    fatal_years = df.groupby([df['Years']])['Fatalities'].sum()
    years = fatal_years.index
    counts = fatal_years.values

    fig,ax = plt.subplots(figsize=(8,6))

    fatal_years.plot(x = 'Years',y = 'Fatalities',ax=ax)
    plt.title('Deaths per Year by Airplane',fontsize=20)
    plt.xlabel('Years')
    plt.ylabel('# of Fatalities')
    plt.setp(ax.get_xticklabels(),rotation='vertical')
    plt.show()

def get_operator_deaths(df):
    fatal_operator = df[['Operator','Fatalities']].groupby(['Operator']).sum()
    fatal_operator = fatal_operator['Fatalities'].sort_values(ascending=False)[:10]

    operators = fatal_operator.index
    deaths = fatal_operator.values
    fig,ax = plt.subplots(figsize=(8,6))
    ind = np.arange(len(operators))
    ax.bar(ind, deaths)

    plt.title('Operator vs Fatalities',fontsize=20)
    plt.xlabel('Operators')
    plt.ylabel('# of Deaths')
    plt.xticks(ind, operators)
    plt.subplots_adjust(bottom=0.40)
    plt.setp(ax.get_xticklabels(),rotation='vertical')
    plt.show()

def deaths_per_accident(df):
    f_sum = df[['Operator','Fatalities']].groupby('Operator').agg(['sum','count'])
    f_sum = f_sum['Fatalities'].reset_index()
    f_sum['Fatalities per Accident'] = f_sum['sum']/f_sum['count']
    f_sum.columns = ['Operator','Fatalities','Accidents','Fatalities per Accident']

    fig, ax = plt.subplots(figsize=(10,6))
    fig.suptitle('Average Fatalities per Accident with at least {} Accidents'.format(5),fontsize=20)
    props = f_sum[f_sum['Accidents'] > 5]

    props[:50].sort_values('Fatalities per Accident',ascending=False).plot(x = 'Operator', \
    y = 'Fatalities per Accident', ax = ax, kind = 'bar', width = .87, grid = True)
    plt.subplots_adjust(bottom=0.50)

    plt.show()


def main():
    #get_deaths_per_year_2(a_df)
    #get_operator_deaths(a_df)
    deaths_per_accident(a_df)
if __name__ == '__main__':
    main()
