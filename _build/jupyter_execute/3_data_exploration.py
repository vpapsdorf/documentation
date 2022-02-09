#!/usr/bin/env python
# coding: utf-8

# # Daten explorieren

# In[1]:


# colors

# neutral
light_grey = '#eeeeee'
grey = '#b3b3b3'
dark_grey = '#666666'
white = '#ffffff'

# reading habits
red = '#810a26'
dark_red = '#4c0a18'
light_red = '#b00e34'

# publishers
green = '#827C17'
light_green = '#979348'

# libraries
blue = '#176682'
light_blue = '#63B2CF'
dark_blue = '#10475b'


# ## Grafiken erstellen

# In[2]:


# import modules
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#import plotly.express as px


# In[34]:


df = pd.read_csv('./data/ebooks_data.csv', delimiter=',', header=[0])
df['year'] = df['year'].astype(np.datetime64)

gfk_df_data = pd.read_csv('./data/gfk_data.csv', delimiter=',', header=[0])


# ### Wie viele aktive Bibliotheksnutzer*innen gibt es in Deutschland?
# Diese Grafik wurde in der Präsentation nicht verwendet.

# In[35]:


fig = go.Figure()

# lenders
fig.add_trace(go.Scatter(x=df['year.1'], y=df['perc_lenders'], name='aktive Bibliotheksnutzer*innen', line=dict(color=light_blue, width=2), showlegend=False, mode='lines+text'))
fig.add_trace(go.Scatter(x=df['year.1'][:-1], y=df['perc_lenders'], name='aktive Bibliotheksnutzer*innen', line=dict(color=blue, width=2), mode='lines+text'))

perc_lenders_2010 = f"{round(df['perc_lenders'][0]*100, 1)} %"
fig.add_annotation(x=2010, y=0.15, text=perc_lenders_2010, showarrow=False, font=dict(size=12, color=blue), bgcolor=white)
perc_lenders_2019 = f"{round(df['perc_lenders'][9]*100, 1)} %"
fig.add_annotation(x=2019, y=0.15, text=perc_lenders_2019, showarrow=False, font=dict(size=12, color=blue), bgcolor=white,)

# annotation for covid-19
fig.add_annotation(x=2020, y=0.9, text="Covid-19", showarrow=False, font=dict(size=12, color=dark_grey))
fig.add_vrect(x0='2019.5', x1='2020.5', fillcolor=light_grey, opacity=0.2, line=dict(color=dark_grey, width=1))

fig.update_layout(title='Aktive Bibliotheksnutzer*innen',
                    title_font_size=25,
                    
                    xaxis_title='Jahr',
                    yaxis_title='Anteil an Gesamtbevölkerung',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=700,
                    showlegend=False,
                   )

fig.update_xaxes(title_text='Jahr', ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, dtick=0.25, ticks='inside', tickformat=".0%", fixedrange=True, range=[0,1], tickcolor=grey, linecolor=grey)

fig.show()


# ### Wie groß ist der Anteil der aktiven Leser*innen - gesamt und digital?
# Diese Grafik wurde in der Präsentation verwendet.

# In[36]:


fig = go.Figure()

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
                    yaxis_title='Anteil an Gesamtbevölkerung in %',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=600,
                    showlegend=False,
                   )

# axes
fig.update_xaxes(title_text='Jahr', ticks='outside', tick0=2017, dtick=3, tickcolor=grey, fixedrange=True, tickwidth=2)
fig.update_yaxes(range=[0,1], tickformat='.0%', dtick=1, visible=False)

fig.show()


# ### Wie hoch ist der Anteil an aktiven Bibliotheksnutzer*innen an aktiven Leser\*innen?
# Diese Grafik wurde in der Präsentation verwendet.

# In[37]:


fig = go.Figure()

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
                    width=800,
                    barmode='stack',
                   )

# axes
fig.update_xaxes(title_text='Jahr', ticks='outside', tick0=2017, tickcolor=grey, fixedrange=True, linecolor=grey)
fig.update_yaxes(range=[0,1], tickformat='.0%', dtick=1)
                   
fig.show()


# ### Wie viele Bücher werden ausgeliehen/gekauft (aufgeschlüsselt)?
# Diese Grafik wurde in der Präsentation (Dashboard) verwendet.

# In[38]:


fig = go.Figure()

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

fig.add_hrect(y0=0, y1=100000000, fillcolor=grey, opacity=0.2, line=dict(color=dark_grey, width=1))

# layout
fig.update_layout(title='Verkaufs- und Entleihzahlen',
                    title_font_size=25,
                    
                    xaxis_title='Jahr',
                    yaxis_title='Anzahl Bücher',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=700,
                    showlegend=False,
                   )

fig.update_xaxes(title_text='Jahr', ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', tickcolor=grey, linecolor=grey, range=[0,420000000])

fig.show()


# ### Wie viele Bücher werden pro gekauftes Buch entliehen - analog und digital?
# Diese Grafik wurde in der Präsentation nicht verwendet.

# In[39]:


fig = go.Figure()

category = ['analog', 'digital']
mean_lendings = [df['lendings_per_sale'].mean(axis=0), df['ebook_lendings_per_sale'].mean(axis=0)]

fig.add_trace(go.Bar(x=category, y=mean_lendings, name='Verkäufe', showlegend=False, marker_color=blue, width=0.4))

fig.update_layout(title='Entliehene Bücher pro gekauftes Buch',
                    title_font_size=25,
                    yaxis_title='Anzahl Bücher',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=500,
                    showlegend=False,
                   )

fig.update_xaxes(fixedrange=True, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', range=[0,1], fixedrange=True, tickcolor=grey, linecolor=grey)


# ### Wie verändern sich die Ausleih- und Verkaufszahlen in den letzten Jahren?
# Diese Grafik wurde in der Präsentation (Dashboard) verwendet.

# In[40]:


fig = go.Figure()

# lendings and sales
fig.add_trace(go.Bar(x=df['year.1'][:8], y=df['lendings_change'], name='Entleihungen', marker_color=blue))
fig.add_trace(go.Bar(x=df['year.1'][:8], y=df['sales_change'], name='Verkäufe', marker_color=green))

fig.update_layout(title='Entleih- und Verkaufszahlen',
                    title_font_size=25,
                    xaxis_title='Jahr',
                    yaxis_title='Anzahl der Bücher',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    width=700,
                   )

fig.update_xaxes(title_text='Jahr', range=[2010.5, 2017.5], ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig.update_yaxes(tick0=0, ticks='inside', range=[-11000000,7500000], fixedrange=True, tickcolor=grey, linecolor=grey)

fig.show()


# ### Wie ist das Kaufverhalten der aktiven Buchkäufer*innen (aufgeschlüsselt)?
# Diese Grafik wurde in der Präsentation (Dashboard) verwendet.

# In[41]:


fig1 = px.bar(gfk_df_data, x="buyer", y="purchases_per_buyer", color='medium', barmode='group',
                    color_discrete_map={
                        'analog': light_red,
                        'digital': dark_red,
                    })
                    
fig1.add_trace(go.Scatter(x=['Gesamt', "Entleiher*innen digital"], y=[0.15, 0.15], mode='lines', line=dict(color=red, width=1), showlegend=False))

fig1.update_layout(title='Kaufverhalten',
                    title_font_size=25,
                    xaxis_title='Art der Käufer*innen',
                    yaxis_title='Durchschnittl. Anzahl an Büchern',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    width=700,
                    plot_bgcolor=white,
                    legend_title_text='Art des Buchs'
                )

fig1.update_xaxes(fixedrange=True, linecolor=grey, dtick=1)
fig1.update_yaxes(tick0=0, ticks='inside', range=[0,1], tickcolor=grey, linecolor=grey, tickformat='.2')


# ### Wie ist das Kaufverhalten von Bibliotheksnutzer*innen (Übersicht)?
# Diese Grafik wurde in der Präsentation (Dashboard) verwendet.

# In[43]:


my_df = gfk_df_data.groupby(['buyer']).mean()
fig1 = px.bar(gfk_df_data.groupby(['buyer']).mean(), y="purchases_per_buyer")
fig1.show()


# In[ ]:




