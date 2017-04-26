import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', \
9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

plt.style.use('ggplot')

a_df = pd.read_csv('AviationDataEnd2016UP.csv',encoding = "ISO-8859-1")

a_df['times'] = a_df['Event.Date'].astype('datetime64[ns]')
a_df['month'] = a_df['times'].map(lambda x: months[x.month])
a_df['year'] = a_df['times'].map(lambda x: x.year)

def month_freq(df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.title('Total Monthly Accidents (1908-2016)',fontsize=20)
    a_df['month'].value_counts().plot(ax=ax, kind='bar')
    plt.show()

def cause_of_accident(df):
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.title('Stages of Flight',fontsize=20)
    a_df['Broad.Phase.of.Flight'].value_counts().plot(ax=ax, kind='bar')
    plt.subplots_adjust(bottom=0.40)
    plt.show()

def accidents_2016(df):
    fatal_years = df.drop_duplicates("Event.Id").groupby([df['year']])['Total.Fatal.Injuries'].sum()
    years = fatal_years[6:].index
    counts = fatal_years[6:].values
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.title('Total Accidents (1982-2016)',fontsize=20)
    ax.plot(years, counts)
    plt.show()

def damage_taken(df):
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.title('Overall Aircraft Damage',fontsize=20)
    a_df['Aircraft.Damage'].value_counts().plot(ax=ax, kind='bar')
    plt.subplots_adjust(bottom=0.40)
    plt.show()

def investigation_type(df):
    fatal_years = a_df[['year','Investigation.Type']].sort_values('year')[6:]

    accidents =  fatal_years.loc[fatal_years['Investigation.Type'] == 'Accident']
    incidents = fatal_years.loc[fatal_years['Investigation.Type'] == 'Incident']

    fig, ax = plt.subplots(figsize=(9, 6))
    plt.title('Accidents vs Incidents',fontsize=20)
    a = Series(accidents['year'].values,accidents['Investigation.Type'].values)
    i = Series(incidents['year'].values,incidents['Investigation.Type'].values)
    a.value_counts().plot(ax=ax)
    i.value_counts().plot(ax=ax, color='b')
    ax.legend(['Accidents','Incidents'], loc='upper right')
    plt.subplots_adjust(bottom=0.40)
    plt.show()


def main():
    #month_freq(a_df)
    #cause_of_accident(a_df)
    #accidents_2016(a_df)
    #damage_taken(a_df)
    investigation_type(a_df)

if __name__ == '__main__':
    main()
