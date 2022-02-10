#!/usr/bin/env python
# coding: utf-8

# # Daten visualisieren
# ## Design
# Da es sich um die Beratung des Bundesrats handelt, ist das Design daran angelehnt.
# 
# ### Schrift
# Auf der [Seite des Bundesrats](https://www.bundesrat.de/DE/homepage/homepage-node.html) ist sowohl serifenlose als auch Serifenschrift zu finden. Da beide Möglichkeiten offen stehen, wird in den im Projekt gezeigten Grafiken Serifenschrift verwendet. Für Fließtext wird eine serifenlose Schrift bevorzugt, weshalb die Absätze im Report in Arial verfasst sind.
# 
# ### Farben
# Auf der [Seite des Bundesrats](https://www.bundesrat.de/DE/homepage/homepage-node.html) lassen sich vornehmlich folgende Farben finden:
# | Farbname | HEX |
# | --- | --- |
# | Rot | #810a26 |
# | Dunkelrot | #4c0a18 |
# | Hellgrau | #eeeeee |
# | Dunkelgrau | #666666 |
# | Weiß | #ffffff |
# 
# Ein noch dunkleres Grau wurde für die Präsentation und den Report verwendet.
# 
# Zur besseren Visualisierung wird in den Grafiken auch noch ein heller Rotton und ein weiterer Grauton verwendet:
# | Farbname | HEX |
# | --- | --- |
# | Hellrot | #b00e34 |
# | Grau | #b3b3b3 |

# In[1]:


""" # colors

# neutral
light_grey = '#eeeeee'
grey = '#b3b3b3'
dark_grey = '#666666'
white = '#ffffff'

# reading habits
red = '#810a26'
dark_red = '#4c0a18'
light_red = '#b00e34' """

print('_')


# ## Grafiken erstellen
# Leider können die Garfiken nicht ausgegeben weden, weil sie in der Umgebung von jupyter-book nicht funktioniert. Ich habe versucht, die Module dort zu installieren bzw. jupyter-book in der base-Umgebung, allerdings hat nichts funktioniert. Dafür werden die statischen Bilder angezeigt.

# In[2]:


""" # import modules
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go """

print('_')


# Zunächst muss die csv-Datei geladen und als Dataframe gespeichert werden.

# In[3]:


""" df = pd.read_csv('./data/ebooks_data.csv', delimiter=',', header=[0])
df['year'] = df['year'].astype(np.datetime64)

gfk_df_data = pd.read_csv('./data/gfk_data.csv', delimiter=',', header=[0]) """

print('_')


# ### Wie groß ist der Anteil der aktiven Leser*innen - gesamt und digital?
# - Slope Graph, damit zu erkennen ist, dass die Entwicklung nicht besonders dynamisch ist
# - Um die Entwicklung sind die einzelnen Werte nicht relevant, deshalb ist es kein Liniendiagramm
# - Zur Orientierung ist die 0%- und 100%-Grenze gekennzeichnet. Zudem ist die y-Achse benannt
# 
# ![Grafik](images/readers.svg)

# In[4]:


""" fig = go.Figure()

# preparation
year_list = [df['year.1'].iloc[-4], df['year.1'].iloc[-1]] # 2017 and 2020

# two traces for readers and digital readers
fig.add_trace(go.Scatter(x=year_list,
                            name='Leser*innen gesamt',
                            y=[df['perc_readers'].iloc[-4], df['perc_readers'].iloc[-1]],
                            mode='lines+markers+text', 
                            text=[f"{round(df['perc_readers'].iloc[-4]*100, 1)} %", f"{round(df['perc_readers'].iloc[-1]*100, 1)} %"],
                            textposition=['top center', 'top center'],
                            line_color=red))

fig.add_trace(go.Scatter(x=year_list,
                            name='Leser*innen digital',
                            y=[df['perc_digital_readers'].iloc[-4], df['perc_digital_readers'].iloc[-1]],
                            mode='lines+markers+text', 
                            text=[f"{round(df['perc_digital_readers'].iloc[-4]*100, 1)} %", f"{round(df['perc_digital_readers'].iloc[-1]*100, 1)} %"],
                            textposition=['top center', 'top center'],
                            line_color=dark_red))

fig.update_traces(hovertemplate='%{x}')

# guiding traces
fig.add_trace(go.Scatter(x=year_list, y=[0, 0], mode='lines', line=dict(color=grey, width=2), showlegend=False))
fig.add_trace(go.Scatter(x=year_list, y=[1, 1], mode='lines', line=dict(color=grey, width=2), showlegend=False))

# annotations with trace names
fig.add_annotation(x=2018.5, y=0.45, text='Leser*innen gesamt', showarrow=False, font=dict(size=14, color=red))
fig.add_annotation(x=2018.5, y=0.15, text='Leser*innen digital', showarrow=False, font=dict(size=14, color=dark_red))

fig.update_layout(title='Leseverhalten der Deutschen',
                    title_font_size=25,
                    xaxis_title='Jahr',
                    yaxis_title='Anteil an Gesamtbevölkerung',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=700,
                    showlegend=False,
                   )

# axes
fig.update_xaxes(title_text='Jahr', ticks='outside', tick0=2017, dtick=3, tickcolor=grey, fixedrange=True, tickwidth=2)
fig.update_yaxes(range=[0,1], tickformat='.0%', dtick=1)

fig.show() """

print('_')


# ### Wie hoch ist der Anteil an aktiven Bibliotheksnutzer*innen an aktiven Leser\*innen?
# - Das Balkendiagramm eignet sich, um den Anteil der Bibliotheksnutzer*innen über die Jahre zu zeigen
# - Die aktuellesten, repräsentativen Daten sind hervorgehoben (2019, vor der Covid-19-Pandemie)
# - Da die Bibliotheksnutzung durch die Covid-19-Pandemie zurückgegangen ist, werden die Daten ausgegraut, weil sie nicht belastbar sind
# 
# ![Grafik](images/lenders.svg)

# In[5]:


""" fig = go.Figure()

# preparation
colors1 = [light_red, ] * 3
colors1.append(grey)

colors2 = [light_grey, ] * 4

perc_lenders_readers_2019 = f"{round(df['perc_lenders_readers'][9]*100)} %"
perc_lenders_readers_2020 = f"{round(df['perc_lenders_readers'][10]*100)} %"

# two bar groups lending and non-lending readers
fig.add_trace(go.Bar(x=df['year.1'][7:12], y=df['perc_lenders_readers'][7:12], name='aktive Bibliotheksnutzer*innen', width=0.6, marker_color=colors1))
fig.add_trace(go.Bar(x=df['year.1'][7:12], y=df['perc_nonlending_readers'][7:12], name='keine Bibliotheksnutzer*innen', width=0.6, marker_color=colors2))
fig.update_traces(hovertemplate='%{x}: %{y}')

# annotation for covid-19
fig.add_annotation(x=2020, y=0.05, text="Covid-19", showarrow=False, font=dict(size=12, color=dark_grey))
fig.add_annotation(x=2020, y=0.3, text=perc_lenders_readers_2020, showarrow=False, font=dict(size=12, color=dark_grey), bgcolor=white,
                    opacity=0.8, bordercolor=dark_grey, borderpad=4)

# annotation for 2019, representative data
fig.add_annotation(x=2019, y=0.3, text=perc_lenders_readers_2019, showarrow=False, font=dict(size=12, color=red), bgcolor=white,
                    opacity=0.8, bordercolor=red, borderpad=4)

# layout
fig.update_layout(title='Aktive Bibliotheksnutzer*innen',
                    title_font_size=25,
                    xaxis_title='Jahr',
                    yaxis_title='Anteil an aktiven Leser*innen',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=700,
                    barmode='stack',
                   )

# axes
fig.update_xaxes(title_text='Jahr', ticks='outside', tick0=2017, tickcolor=grey, fixedrange=True, linecolor=grey)
fig.update_yaxes(range=[0,1], tickformat='.0%', dtick=1, linecolor=grey)
                   
fig.show() """

print('_')


# ### Wie verändern sich die Ausleih- und Verkaufszahlen in den letzten Jahren?
# - Das Balkendiagramm eignet sich, um die Veränderung der Zahlen zum Vorjahr zu zeigen
# - Diese Grafik wurde ins Dashboard übertragen, damit man beide Kategorien unabhängig voneinander zeigen kann
# - Zur Orientierung wurde die 0%-Grenze eingezeichnet
# 
# ![Grafik](images/changes_lendings_sales.svg)

# In[6]:


""" fig = go.Figure()

# lendings and sales
fig.add_trace(go.Bar(x=df['year.1'][:8], y=df['lendings_change'], name='Entleihungen', marker_color=red, width=0.3))
fig.add_trace(go.Bar(x=df['year.1'][:8], y=df['sales_change'], name='Verkäufe', marker_color=dark_red, width=0.3))

fig.add_trace(go.Scatter(x=(2010, 2018), y=(0,0), showlegend=False, line_color=dark_grey, line_width=0.3))

fig.update_layout(
                    title="Veränderungen der Verkäufe und Entleihungen zum Vorjahr",
                    title_font_size=25,
                    xaxis_title="Jahr",
                    yaxis_title="Anzahl an Büchern",
                    font_family="Gravitas One",
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=800,
                )

fig.update_xaxes(title_text='Jahr', range=[2010.5, 2017.5], ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', range=[-13000000,13000000], fixedrange=True, tickcolor=grey, linecolor=grey)

fig.show() """

print('_')


# ### Wie viele Bücher werden ausgeliehen/gekauft (aufgeschlüsselt)?
# - Das Liniendiagramm eignet sich, um die Veränderung der Zahlen zum Vorjahr zu zeigen
# - Diese Grafik wurde ins Dashboard übertragen, damit man beide Kategorien unabhängig voneinander zeigen kann
# 
# ![Grafik](images/lendings_purchases.svg)

# In[7]:


""" fig = go.Figure()

# analog
fig.add_trace(go.Scatter(x=df['year.1'][:8], y=df['book_sales'], name='Verkäufe analog', line=dict(color=light_red, width=2), mode='lines+text'))
fig.add_trace(go.Scatter(x=df['year.1'][:8], y=df['print_lendings'], name='Entleihungen analog', line=dict(color=dark_red, width=2), mode='lines+text'))

fig.add_annotation(x=2010.5, y=330000000, text="analog", showarrow=False, font=dict(size=12, color=dark_grey), bgcolor=white, opacity=0.8, bordercolor=dark_grey, borderpad=4)
fig.add_annotation(x=2017, y=350000000, text="Verkäufe", showarrow=False, font=dict(size=12, color=light_red))
fig.add_annotation(x=2017, y=230000000, text="Entleihungen", showarrow=False, font=dict(size=12, color=dark_red))

fig.add_hrect(y0=200000000, y1=420000000, fillcolor=grey, opacity=0.2, line=dict(color=dark_grey, width=1))

#digital
fig.add_trace(go.Scatter(x=df['year.1'][:8], y=df['ebook_sales'], name='Verkäufe digital', line=dict(color=light_red, width=2), mode='lines+text'))
fig.add_trace(go.Scatter(x=df['year.1'][:8], y=df['digital_lendings'], name='Entleihungen digital', line=dict(color=dark_red, width=2), mode='lines+text'))

fig.add_annotation(x=2010.5, y=50000000, text="digital", showarrow=False, font=dict(size=12, color=dark_grey), bgcolor=white, opacity=0.8, bordercolor=dark_grey, borderpad=4)
fig.add_annotation(x=2017, y=50000000, text="Verkäufe", showarrow=False, font=dict(size=12, color=light_red))
fig.add_annotation(x=2017, y=8000000, text="Entleihungen", showarrow=False, font=dict(size=12, color=dark_red))

fig.add_hrect(y0=0, y1=100000000, fillcolor=grey, opacity=0.2, line=dict(color=grey, width=1))

# layout
fig.update_layout(title='Verkaufs- und Entleihzahlen',
                    title_font_size=25,
                    
                    xaxis_title='Jahr',
                    yaxis_title='Anzahl Bücher',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=800,
                    showlegend=False,
                   )

fig.update_xaxes(title_text='Jahr', ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', tickcolor=grey, linecolor=grey, range=[0,420000000])

fig.show() """

print('_')


# ### Wie ist das Kaufverhalten?
# - Das Balkendiagramm eignet sich für die kategorialen Daten
# - Weil die Darstellung recht komplex ist, wurde sie ins Dashboard übernommen
# - Im Dashboard werden die Zahlen der einzelnen Kategorien zunächst summiert und angezeigt (siehe nächste Grafik), also wie viele Bücher insgesamt gekauft werden (siehe unten)
# - Die Aufschlüsselung in analoge und digitale Bücher wird erst danach gezeigt
# 
# 
# ![Grafik](images/buying_habits.svg)

# In[8]:


""" fig = px.bar(gfk_df_data, x="buyer", y="purchases_per_buyer", color='medium', barmode='group',
                    color_discrete_map={
                        'analog': light_red,
                        'digital': dark_red,
                    })
                    
fig.add_trace(go.Scatter(x=['Gesamt', "Entleiher*innen digital"], y=[0.15, 0.15], mode='lines', line=dict(color=red, width=1), showlegend=False))

fig.update_layout(title='Kaufverhalten',
                    title_font_size=25,
                    xaxis_title='Art der Käufer*innen',
                    yaxis_title='Durchschnittl. Anzahl an Büchern',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    width=800,
                    plot_bgcolor=white,
                    legend_title_text='Art des Buchs'
                )

fig.update_xaxes(fixedrange=True, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', range=[0,1], tickcolor=grey, linecolor=grey, tickformat='.2') """

print('_')


# 
# ![Grafik](images/buying_habits2.svg)

# In[9]:


""" overview_df = gfk_df_data.groupby(['buyer']).mean().sort_values(by='buyer', ascending=False)

fig = px.bar(overview_df, y="purchases_per_buyer")
fig.update_traces(marker_color=[red, red, red])

fig.update_layout(title='Kaufverhalten',
                title_font_size=25,
                xaxis_title='Art der Käufer*innen',
                yaxis_title='Anzahl an Büchern',
                font_family='Gravitas One',
                font_color=dark_grey,
                plot_bgcolor=white,
                legend_title_text='Art des Buchs',
                width=600,
            )

fig.update_xaxes(fixedrange=True, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', tickcolor=grey, linecolor=grey, tickformat='.2') """

print('_')

