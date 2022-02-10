#!/usr/bin/env python
# coding: utf-8

# # Excel
# 
# Der Report wurde in Word erstellt und als PDF exportiert. Dazu gibt es ein Excel-Sheet mit den wichtigsten Daten.
# ## Vorbereitung

# In[1]:


""" import pandas as pd

# colors

# neutral
light_grey = '#eeeeee'
grey = '#b3b3b3'
dark_grey = '#666666'
white = '#ffffff'

red = '#810a26'
dark_red = '#4c0a18'
light_red = '#b00e34' """

print('_')


# In[2]:


""" writer = pd.ExcelWriter('report_data.xlsx', engine='xlsxwriter')

# select data
df = pd.read_csv('./data/ebooks_data.csv', delimiter=',', header=[0])
gfk_df_data = pd.read_csv('./data/gfk_data.csv', delimiter=',', header=[0]) """

print('_')


# ## Ausführung
# ### Lesverhalten in Deutschland (Sheet 1)
# Die Zahlen werden eingefärbt, damit man sieht, dass beides leicht zugenommen hat. Zudem wird eine Grafik erstellt.

# In[3]:


# select and alter data
""" df1 = df.loc[7:10, ['year.1', 'readers', 'digital_readers']]
df1['readers'] = df1['readers'].astype(int)
df1['digital_readers'] = df1['digital_readers'].astype(int)
df1.rename(columns={'year.1': 'Jahr', 'readers': 'Leser*innen gesamt', 'digital_readers': 'Leser*innen digital'}, inplace=True)
df1 = df1.set_index('Jahr') """

print('_')


# In[4]:


# write and design data
""" df1.to_excel(writer, sheet_name='Daten1', startrow=2)

book = writer.book
sheet1 = writer.sheets['Daten1']

bold = book.add_format({'bold': True, 'size': 24})
italic = book.add_format({'italic': True})

sheet1.write('A1', 'Leseverhalten in Deutschland', bold)
sheet1.write('A17', 'Basierend auf Daten von IfD Allensbach (2021a, 2021b)', italic)

sheet1.set_column('B:C', 20)

sheet1.conditional_format('B4:B8', {'type': '2_color_scale', 'min_color': light_grey, 'max_color': grey})
sheet1.conditional_format('C4:C8', {'type': '2_color_scale', 'min_color': light_grey, 'max_color': grey}) """

print('_')


# In[5]:


# chart
""" chart1 = book.add_chart({'type': 'column', 'title': 'Leseverhalten in Deutschland'})

chart1.add_series({
    'categories': '=Daten1!A4:A7',
    'values': '=Daten1!B4:B7',
    'name': '=Daten1!B3',
    'fill': {'color': red},
    })
chart1.add_series({
    'categories': '=Daten1!A4:A7',
    'values': '=Daten1!C4:C7',
    'name': '=Daten1!C3',
    'fill': {'color': dark_red}
    })

chart1.set_x_axis({'name': 'Jahr'})

sheet1.insert_chart('F2', chart1) """

print('_')


# ## Aktive Bibliotheksnutzer*innen (Sheet 2)

# In[6]:


# select and alter data
""" df2 = df.loc[7:10, ['year.1', 'lenders']]
df2.rename(columns={'year.1': 'Jahr', 'lenders': 'Bibliotheksnutzer*innen gesamt'}, inplace=True)
df2 = df2.set_index('Jahr') """

print('_')


# In[7]:


# write and design data
""" df2.to_excel(writer, sheet_name='Daten2', startrow=2)

book = writer.book
sheet2 = writer.sheets['Daten2']

bold = book.add_format({'bold': True, 'size': 24})
italic = book.add_format({'italic': True})

sheet2.write('A1', 'Aktive Bibliotheksnutzer*innen', bold)
sheet2.write('A17', 'Basierend auf Daten von IfD Allensbach (2021b) und Deutsche Bibliotheksstatistik (2010–2020)', italic)

sheet2.set_column('B:B', 30) """

print('_')


# In[8]:


# chart
""" chart2 = book.add_chart({'type': 'column', 'title': 'Leseverhalten in Deutschland'})

chart2.add_series({
    'categories': '=Daten2!A4:A7',
    'values': '=Daten2!B4:B7',
    'name': '=Daten2!B3',
    'fill': {'color': red},
    })

chart2.set_x_axis({'name': 'Jahr'})

sheet2.insert_chart('F2', chart2) """

print('_')


# ### Veränderungen der Verläufe und Entleihungen zum Vorjahr (Sheet 3)
# Um sichtbar zu machen, ob die Veränderungen positiv oder negativ war, wurde ein Balken in die einzelnen Zellen eingefügt.

# In[9]:


# select and alter data
""" df3 = df.loc[1:7, ['year.1', 'lendings_change', 'sales_change']]
df3.rename(columns={'year.1': 'Jahr', 'lendings_change': 'Entleihungen', 'sales_change': 'Verkäufe'}, inplace=True)
df3 = df3.set_index('Jahr') """

print('_')


# In[10]:


# write and design data
""" df3.to_excel(writer, sheet_name='Daten3', startrow=2)

book = writer.book
sheet3 = writer.sheets['Daten3']

bold = book.add_format({'bold': True, 'size': 24})
italic = book.add_format({'italic': True})

sheet3.write('A1', 'Veränderungen der Verläufe und Entleihungen zum Vorjahr', bold)
sheet3.write('A12', 'Basierend auf Daten von Börsenverein des Deutschen Buchhandels (2021), Börsenblatt & Börsenverein des Deutschen Buchhandels (2018) und Deutsche Bibliotheksstatistik (2010–2020)', italic)

sheet3.set_column('B:C', 40)

format3 = book.add_format({'font_color': light_red})
sheet3.conditional_format('B4:B10', {'type': 'data_bar', 'bar_solid': True})
sheet3.conditional_format('C4:C10', {'type': 'data_bar', 'bar_solid': True}) """

print('_')


# ### Verkaufs- und Einleihzahlen (Sheet 4)
# Um die Zahlen besser einschätzen zu können, werden die einzelnen Zellen mit Farben versehen. Zudem wurde auch eine Grafik erstellt.

# In[11]:


# select and alter data
""" df4 = df.loc[0:7, ['year.1', 'print_lendings', 'book_sales', 'digital_lendings', 'ebook_sales']]
df4.rename(columns={
    'year.1': 'Jahr',
    'print_lendings': 'Entleihungen analog',
    'book_sales': 'Verkäufe analog',
    'digital_lendings': 'Entleihungen digital',
    'ebook_sales': 'Verkäufe digital'},
    inplace=True)
df4 = df4.set_index('Jahr')
 """
print('_')


# In[12]:


# write and design data
""" df4.to_excel(writer, sheet_name='Daten4', startrow=2)

book = writer.book
sheet4 = writer.sheets['Daten4']

bold = book.add_format({'bold': True, 'size': 24})
italic = book.add_format({'italic': True})

sheet4.write('A1', 'Verkaufs- und Entleihzahlen', bold)
sheet4.write('A17', 'Basierend auf Daten von Börsenverein des Deutschen Buchhandels (2021), Börsenblatt & Börsenverein des Deutschen Buchhandels (2018) und Deutsche Bibliotheksstatistik (2010–2020)', italic)

sheet4.set_column('B:E', 18)

format4 = book.add_format({'font_color': light_red})
sheet4.conditional_format('B4:B11', {'type': '3_color_scale'})
sheet4.conditional_format('C4:C11', {'type': '3_color_scale'})
sheet4.conditional_format('D4:D11', {'type': '3_color_scale'})
sheet4.conditional_format('E4:E11', {'type': '3_color_scale'}) """

print('_')


# In[13]:


# chart
""" chart4 = book.add_chart({'type': 'line', 'title': 'Leseverhalten in Deutschland', 'width': 1000})

chart4.add_series({
    'categories': '=Daten4!A4:A11',
    'values': '=Daten4!B4:B11',
    'name': '=Daten4!B3',
    'line': {'color': light_red},
    })

chart4.add_series({
    'categories': '=Daten4!A4:A11',
    'values': '=Daten4!C4:C11',
    'name': '=Daten4!C3',
    'line': {'color': dark_red},
    })

chart4.add_series({
    'categories': '=Daten4!A4:A11',
    'values': '=Daten4!D4:D11',
    'name': '=Daten4!D3',
    'line': {'color': grey},
    })

chart4.add_series({
    'categories': '=Daten4!A4:A11',
    'values': '=Daten4!E4:E11',
    'name': '=Daten4!E3',
    'line': {'color': dark_grey},
    })

chart4.set_x_axis({'name': 'Jahr'})

sheet4.insert_chart('G2', chart4) """

print('_')


# ### Kaufverhalten (Sheet 5)
# Die einzelnen Kategorien der Art des Buchs werden farblich gekennzeichnet. Zudem wurden Balken in die Zellen der Anzahl der Bücher pro Käufer*in hinzugefügt.

# In[14]:


# select and alter data
""" df5 =gfk_df_data.loc[0:6, ['buyer', 'medium', 'purchases', 'buyer_no', 'purchases_per_buyer']]

df5['purchases_per_buyer'] = round(df5['purchases_per_buyer'], 2)

df5.rename(columns={
    'buyer': 'Käufer*innen',
    'medium': 'Art des Buchs',
    'purchases': 'Durchschnittl. Käufe',
    'buyer_no': 'Anzahl der Käufer*innen',
    'purchases_per_buyer': 'Anz. an Büchern pro Käufer*in'},
    inplace=True) """

print('_')


# In[15]:


# write and design data
""" df5.to_excel(writer, sheet_name='Daten5', startrow=2)

book = writer.book
sheet5 = writer.sheets['Daten5']

bold = book.add_format({'bold': True, 'size': 24})
italic = book.add_format({'italic': True})

sheet5.write('A1', 'Kaufverhalten', bold)
sheet5.write('A11', 'Basierend auf Daten von GfK (2019, S. 35)', italic)

sheet5.set_column('B:F', 25)

format5a = book.add_format({'bg_color': light_red, 'font_color': white})
format5b = book.add_format({'bg_color': dark_red, 'font_color': white})
sheet5.conditional_format('C4:C9', {'type': 'cell', 'criteria': '==', 'value': '"analog"', 'format': format5a})
sheet5.conditional_format('C4:C9', {'type': 'cell', 'criteria': '==', 'value': '"digital"', 'format': format5b})
sheet5.conditional_format('F4:F9', {'type': 'data_bar', 'bar_solid': True}) """

print('_')


# ### Quellen und Excel-Datei speichern

# In[16]:


# write and design data
""" book = writer.book
sheet6 = book.add_worksheet('Quellen')

sheet6.write('A1', 'Börsenblatt & Börsenverein des Deutschen Buchhandels. (2018, 7. Juni). Absatz von Büchern in Deutschland in den Jahren 2004 bis 2017 (in Millionen Titel) [Graph]. In Statista. Zugriff am 09. Februar 2022, von https://de.statista.com/statistik/daten/studie/416380/umfrage/absatz-von-buechern-in-deutschland/')
sheet6.write('A2', 'Börsenverein des Deutschen Buchhandels. (2021, 9. September). Absatz von E-Books im Publikumsmarkt in Deutschland in den Jahren 2010 bis zum 1. Halbjahr 2021 (in Millionen Stück) [Graph]. In Statista. Zugriff am 09. Februar 2022, von https://de.statista.com/statistik/daten/studie/232191/umfrage/absatz-von-e-books-in-deutschland/')
sheet6.write('A3', 'Deutsche Bibliotheksstatistik. (2010–2020). Variable Auswertung (eigens erstellt) [Datensatz]. Deutsche Bibliotheksstatistik. https://www.bibliotheksstatistik.de/')
sheet6.write('A4', 'GfK. (2019, November). Wer leiht was in Bibliotheken und insbesondere online? Börsenverein des Deutschen Buchhandels. https://www.boersenverein.de/tx_file_download?tx_theme_pi1%5BfileUid%5D=3840&tx_theme_pi1%5Breferer%5D=https%3A%2F%2Fwww.boersenverein.de%2Fmarkt-daten%2Fmarktforschung%2Fstudien-umfragen%2Fstudie-zur-onleihe-2019%2F&cHash=5e0d2b87985fa82117a341edfad37027')
sheet6.write('A5', 'IfD Allensbach. (2021a, 28. Juni). Anzahl der Personen in Deutschland, die Bücher auf elektronischen Geräten (E-Reader, Tablet-PC, Smartphone) lesen, von 2017 bis 2021 (in Millionen) [Graph]. In Statista. Abgerufen am 09. Januar 2022, von https://de.statista.com/statistik/daten/studie/265230/umfrage/e-reader-tablet-smartphone-lesen-von-buechern-auf-elektronischen-geraeten/')
sheet6.write('A6', 'IfD Allensbach. (2021b, 28. Juni). Anzahl der Personen in Deutschland, die Bücher lesen, nach Häufigkeit von 2017 bis 2021 (in Millionen) [Graph]. In Statista. Abgerufen am 09. Januar 2022, von https://de.statista.com/statistik/daten/studie/171231/umfrage/haeufigkeit-des-lesens-von-einem-buch/')

sheet6.set_column('A:A', 250) """

print('_')


# In[17]:


""" # save
writer.save() """

print('_')

