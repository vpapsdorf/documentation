#!/usr/bin/env python
# coding: utf-8

# # Daten aufbereiten
# 

# In[1]:


# import modules
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype


# ### Bibliotheken

# In[2]:


library_df = pd.read_csv('./data/dbs_data.csv', delimiter=';', header=[2,3], encoding='ISO-8859-1', low_memory=False)


# Die Angaben sind nach einzelnen Bibliotheken aufgeschlüsselt. Nur die Ergebniszeile mit der Summe der Ergebnisse ist relevant.

# In[3]:


# just relevant data
sum_row = library_df.loc[(library_df[('NR','Unnamed: 0_level_1')] == 'Summe')]
library_df = sum_row.astype('string')
library_df


# Das Dataframe soll so aufgebaut sein, dass jede Zeile ein Jahr darstellt. In den Spalten finden sich die Ausprägungen wie zum Beispiel die Anzahl der Bibliotheksnutzer*innen.

# In[4]:


# shape dataframe
library_df = pd.melt(library_df)
library_df = library_df.rename(columns={"variable_0": "variable", 'variable_1': 'year', 'value': 'value'})
library_df = library_df.drop([0, 1, 2, 3, 92])
library_df = library_df.pivot(index='year', columns='variable', values='value')


# Die Datentypen müssen noch angepasst werden.

# In[5]:


# replace decimal comma and thousand delimiter
for label, content in library_df.iteritems():
    library_df[label] = library_df[label].str.replace('.', '', regex=True)
    library_df[label] = library_df[label].str.replace(',', '.', regex=True)

# turn into floats
for label, content in library_df.iteritems():
    library_df[label] = library_df[label].astype(float)


# ### Bevölkerung

# In[6]:


pop_df = pd.read_csv('./data/pop_data.csv', delimiter=';', encoding='ISO-8859-1', header=[5])


# Im Datensatz befinden sich einige Zeilen, die keine relevanten Informationen enthalten. Zudem müssen die Beschriftungen und Datentypen angepasst werden.

# In[7]:


# just relevant data
pop_df = pop_df.drop([11, 12, 13, 14])

# rename columns
pop_df = pop_df.rename(columns={"Unnamed: 0": "year", "Anzahl": "population"})

# change datatypes
pop_df['population'] = pop_df['population'].astype(int)
pop_df['date'] = pd.to_datetime(pop_df['year'], format='%d.%m.%Y')
pop_df = pop_df.set_index(pop_df['year'])


# ### Zusammenfassung mit weiteren Daten
# Im Dataframe werden die zwei Dataframes zusammengefasst. Zudem werden einige Daten, die nicht als Datensatz zur Verfügung stehen, händisch eingetragen.

# In[8]:


df = pd.DataFrame(
    {
        # general info
        'year' : ([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]),
        'population' : pop_df['population'],

        # reading habits
        'digital_readers': ([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 7650000, 8520000, 8680000, 9120000]),

        'readers_weekly' : ([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11640000, 11930000, 11960000, 12620000]),
        'readers_monthly' : ([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15070000, 14840000, 14730000, 14710000]),
        'readers_once_month' : ([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6870000, 7060000, 7110000, 7030000]),

        # publishing information
        'ebook_sales': ([1900000, 4300000, 13200000, 21500000, 24800000, 27000000, 28100000, 29100000, 32800000, 32400000, 35800000]),
        'book_sales': ([416000000, 401000000, 399000000, 398000000, 387000000, 380000000, 377000000, 367000000, np.nan, np.nan, np.nan]),

        # library information
        'lenders': library_df['Entleiher'].values.astype(int),
        'lendings': library_df['Entleih. insges.'].values.astype(int),
        'digital_lendings': library_df['Entl. virt.Best.'].values.astype(int),
        'ebook_lendings': ([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 25652538, 30211532]),
        'print_lendings': library_df['Entl. Print'].values,
        
    }
)


# ### Neue Daten aggregieren

# Zur Datenexploration werden noch weitere Daten aggregiert.

# In[9]:


# total lendings and sales of books
df['sales'] = df['ebook_sales'] + df['book_sales']
df['lendings'] = df['digital_lendings'] + df['print_lendings']

# regular readers
df['readers'] = df['readers_weekly'] + df['readers_monthly'] + df['readers_once_month']

# readers relative to the population over the years
df['perc_digital_readers'] = df['digital_readers'] / df['population']
df['perc_readers'] = df['readers'] / df['population']
df['perc_lenders'] = df['lenders'] / df['population']

# lenders relative to the reading population
df['perc_lenders_readers'] = df['lenders']/df['readers']
df['perc_nonlending_readers'] = 1-(df['lenders']/df['readers'])

# lendings and sales per population
df['lendings_per_person'] = df['lendings']/df['population']
df['sales_per_person'] = df['sales']/df['population']

# change in sales and lendings
df['sales_change'] = df['sales'].diff()
df['lendings_change'] = df['lendings'].diff()

# lending or sale of ebook per digital reader
df['lendings_per_digital_reader'] = df['ebook_lendings']/df['digital_readers']
df['sales_per_digital_reader'] = df['ebook_sales']/df['digital_readers']

# lendings per sale
df['lendings_per_sale'] = df['lendings']/df['sales']
df['ebook_lendings_per_sale'] = df['ebook_lendings']/df['ebook_sales']


# ### GfK-Studie
# Da diese Daten nur grafisch dargestellt sind und nicht als Datensatz verfügbar sind, werden sie händisch eingetragen.

# In[10]:


gfk_df = pd.DataFrame(
    data={
        'medium':['analog', 'digital', 'analog', 'digital', 'analog', 'digital'],
        'purchases':[27.8, 3.7, 5.9, 0.5, 1.5, 0.4],
        'buyer_no':[29.6, 29.6, 9.2, 9.2, 2.6, 2.6],
        'buyer':['Gesamt', 'Gesamt', 'Entleiher*innen analog', 'Entleiher*innen analog', 'Entleiher*innen digital', 'Entleiher*innen digital']
    }
)

gfk_df['purchases_per_buyer'] = gfk_df['purchases']/gfk_df['buyer_no']


# Diese Daten enthalten kategoriale Werte, die eine Ordnung haben.

# In[11]:


cat_habits = CategoricalDtype(categories=['nicht mehr', 'seltener', 'genau so oft', 'öfter', 'noch nie'], ordered=True)

buying_habits_df = pd.DataFrame(
    data={
        'medium':['analog', 'analog', 'analog', 'analog', 'analog', 'digital', 'digital', 'digital', 'digital', 'digital'],
        'buying_habits': ['nicht mehr', 'seltener', 'genau so oft', 'öfter', 'noch nie', 'nicht mehr', 'seltener', 'genau so oft', 'öfter', 'noch nie'],
        'percentage':[10, 33, 48, 4, 6, 13, 16, 22, 11, 38]
    }
)

buying_habits_df['buying_habits'] = buying_habits_df['buying_habits'].astype(cat_habits)
buying_habits_df['medium'] = pd.Categorical(buying_habits_df['medium'])


# ### Daten speichern
# Die Dataframes als csv-Dateien speichern.

# In[12]:


df.to_csv('./data/ebooks_data.csv')
df.to_csv('./app/data/ebooks_data.csv')


# In[ ]:


gfk_df.to_csv('./data/gfk_data.csv')
gfk_df.to_csv('./app/data/gfk_data.csv')


# In[ ]:


buying_habits_df.to_csv('./data/purchase_data.csv')
buying_habits_df.to_csv('./app/data/purchase_data.csv')

