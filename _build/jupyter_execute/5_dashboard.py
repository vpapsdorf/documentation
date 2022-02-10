#!/usr/bin/env python
# coding: utf-8

# # Dashboard (Präsentation)
# Die Präsentation wurde mit PowerPoint erstellt. Das Dashboard enthält alle Grafiken im Abschnitt "Analyse" der Präsentation. So muss nicht ständig zwischen PowerPoint und dem Dashboard gewechselt. Zudem ist es besonders geschickt, weil man auch mit den Grafiken interagieren kann.
# 
# ## Desgin
# In der Präsentation/im Dashboard wurden das gleiche Design wie bei der Erstellung der Grafiken verwendet. Für den Teil der Präsentation, welcher nicht so stark auf Daten beruht, wurde möglichst wenig Text verwendet und viel auf Icons zurückgegriffen. Ist eine Grafik auf einer Folie zu sehen, wurde zur Einordnung ein Satz eingeblendet, der die Kerninformation transportiert.
# 
# ## Erstellen des Dashboards
# Das Dashboard basiert auf einer App aus den Vorlesungsmaterialien. Die Grafiken waren bereits erstellt und wurden nur noch angepasst, damit sie zum Dashboard passen. dIe Tab-Bestandteile wurden vom Beispiel der [Plotly-Website](https://dash.plotly.com/dash-core-components/tabs) (Abschnitt Method 2. Content as Tab Children) entnommen und an die bereits bestehende App angepasst. Wie in der PowerPoint-Präsentation wurde zu jeder Grafik wurde ein Satz verfasst, welcher die Kerninformationen zusammenfasst.
# 
# ## Interaktivität und Einbinden in die Story
# Das Dashboard hat einen statischen Header und Hintergrund. Die Inhalte sind in drei Tabs unterteilt, damit man zwischen diesen möglichst leicht springen kann.
# - Im ersten Tab wird vor allem das Anklicken der Legendenbezeichnungen genutzt
# - Im zweiten Tab wird mit der Grafik interagiert, indem man wichtige Stellen fokussiert und heranzoomt
# - Im letzten Tab wird nicht nur die Interaktivität der Plotly-Grafiken genutzt, sondern auch die der Dash-App. So verändert sich die Grafik je nach Auswahl im Dropdown-Menü
# 
# ## Ergebnis

# In[1]:


""" import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from plotly import graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output


# colors
light_grey = "#eeeeee"
grey = "#b3b3b3"
dark_grey = "#666666"
white = "#ffffff"
red = "#810a26"
dark_red = "#4c0a18"
light_red = '#b00e34'

df = pd.read_csv("./data/ebooks_data.csv", delimiter=",", header=[0])
gfk_df_data = pd.read_csv('./data/gfk_data.csv', delimiter=',', header=[0])



fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["year.1"][:8],
        y=df["lendings_change"],
        name="Entleihungen",
        marker_color=dark_red,
        width=0.3,
    )
)
fig.add_trace(
    go.Bar(
        x=df["year.1"][:8],
        y=df["sales_change"],
        name="Verkäufe",
        marker_color=red,
        width=0.3,
    )
)
fig.update_layout(
    title="Veränderungen der Verkäufe und Entleihungen zum Vorjahr",
    title_font_size=25,
    xaxis_title="Jahr",
    yaxis_title="Anzahl an Büchern",
    font_family="Gravitas One",
    font_color=dark_grey,
    plot_bgcolor=white,
)
fig.add_shape(type='line', y0=0, y1=0, x0=0, x1=2100, line=dict(color=grey, width=0.5), xref='x', yref='y',)

fig.update_xaxes(
    title_text="Jahr",
    range=[2010.5, 2017.5],
    ticks="inside",
    fixedrange=True,
    tickcolor=grey,
    tickwidth=1,
    linecolor=grey,
    dtick=1,
)
fig.update_yaxes(
    tick0=0,
    ticks="inside",
    range=[-14000000, 8000000],
    fixedrange=True,
    tickcolor=grey,
    linecolor=grey,
)



fig_sales = go.Figure()

# analog
fig_sales.add_trace(go.Scatter(x=df['year.1'][:8], y=df['book_sales'], name='Verkäufe analog', line=dict(color=light_red, width=2), mode='lines+text'))
fig_sales.add_trace(go.Scatter(x=df['year.1'][:8], y=df['print_lendings'], name='Entleihungen analog', line=dict(color=dark_red, width=2), mode='lines+text'))

fig_sales.add_annotation(x=2010.5, y=330000000, text="analog", showarrow=False, font=dict(size=12, color=dark_grey), bgcolor=white, opacity=0.8, bordercolor=dark_grey, borderpad=4)
fig_sales.add_annotation(x=2017, y=350000000, text="Verkäufe", showarrow=False, font=dict(size=12, color=light_red))
fig_sales.add_annotation(x=2017, y=230000000, text="Entleihungen", showarrow=False, font=dict(size=12, color=dark_red))

#digital
fig_sales.add_trace(go.Scatter(x=df['year.1'][:8], y=df['ebook_sales'], name='Verkäufe digital', line=dict(color=light_red, width=2), mode='lines+text'))
fig_sales.add_trace(go.Scatter(x=df['year.1'][:8], y=df['digital_lendings'], name='Entleihungen digital', line=dict(color=dark_red, width=2), mode='lines+text'))

fig_sales.add_annotation(x=2010.5, y=50000000, text="digital", showarrow=False, font=dict(size=12, color=dark_grey), bgcolor=white, opacity=0.8, bordercolor=dark_grey, borderpad=4)
fig_sales.add_annotation(x=2017, y=50000000, text="Verkäufe", showarrow=False, font=dict(size=12, color=light_red))
fig_sales.add_annotation(x=2017, y=8000000, text="Entleihungen", showarrow=False, font=dict(size=12, color=dark_red))

# layout
fig_sales.update_layout(title='Verkaufs- und Entleihzahlen',
                    title_font_size=25, 
                    xaxis_title='Jahr',
                    yaxis_title='Anzahl Bücher',
                    font_family='Gravitas One',
                    font_color=dark_grey,
                    plot_bgcolor=white,
                    showlegend=False,
                   )

fig_sales.update_xaxes(title_text='Jahr', ticks='inside', fixedrange=True, tickcolor=grey, tickwidth=1, linecolor=grey, dtick=1)
fig_sales.update_yaxes(tick0=0, ticks='inside', tickcolor=grey, linecolor=grey, range=[0,420000000])


app = dash.Dash(__name__, title="Analyse | Bundesrat")

app.layout = html.Div(
    [
        html.Div(
            className="app-header",
            children=[
                html.Div("Die gesetzliche Gleichstellung von digitalen und analogen Büchern", className="app-header--title"),
                html.Img(src="./assets/bundesrat.png", className="app-header"),
            ],
        ),
        html.Div([
            dcc.Tabs([
                dcc.Tab(label='Welcher Zusammenhang besteht zwischen Entleihungen und Verkäufen?', children=[
                    html.H3('Es scheint generell keinen erkennbaren Zusammenhang zwischen Entleihungen und Verkäufen zu geben.'),
                    html.Div(
                                [
                                    dcc.Graph(figure=fig),
                                ],
                                className="graph",
                            ),
                    html.Hr(),
                    html.P('Abbildung 3: Veränderungen der Verkäufe und Entleihungen zum Vorjahr.'),
                    html.P('Basierend auf Daten von Börsenverein des Deutschen Buchhandels (2021), Börsenblatt & Börsenverein des Deutschen Buchhandels (2018) und Deutsche Bibliotheksstatistik (2010–2020).'),
                ],
                className ='custom-tab',
                selected_className='custom-tab--selected'
                ),
                dcc.Tab(label='Inwiefern unterscheiden sich Entleihungen und Verkäufe im Hinblick auf digitale und analoge Bücher?', children=[
                    html.H3('Im Verhältnis zu analogen Büchern und zu digitalen Entleihungen werden E-Books eher selten gekauft.'),
                    html.Div(
                                [
                                    dcc.Graph(figure=fig_sales),
                                ],
                                className="graph",
                            ),
                    html.Hr(),
                    html.P('Abbildung 4: Veränderungen der Verkäufe und Entleihungen.'),
                    html.P('Basierend auf Daten von Börsenverein des Deutschen Buchhandels (2021), Börsenblatt & Börsenverein des Deutschen Buchhandels (2018) und Deutsche Bibliotheksstatistik (2010–2020).'),
                ],
                className ='custom-tab',
                selected_className='custom-tab--selected'
                ),

                dcc.Tab(label='Wer kauft digitale Bücher?', children=[
                    html.H3('Das Entleihen von digitalen Bücher scheint den Kauf von digitalen Büchern nicht zu hemmen.'),
                    dcc.Dropdown(
                        className="input",
                        id="comparison",
                        options=[
                            {"label": "Kaufverhalten insgesamt", "value": 0},
                            {"label": "Kaufverhalten aufgeschlüsselt", "value": 1},
                        ],
                        value=0,
                    ),
                    html.Div(
                                [
                                    dcc.Graph(id="graph1"),
                                ],
                                className="graph",
                            ),
                    html.Hr(),
                    html.P('Abbildung 5: Kaufverhalten aufgeschlüsselt nach verschiedenen Faktoren.'),
                    html.P('Basierend auf Daten von GfK (2019, S. 35)'),
                ],
                className ='custom-tab',
                selected_className='custom-tab--selected'
                ),
            ])
        ],
        className='app-main'),
    ],
)


@app.callback(
    Output("hover-data", "children"), Input("basic-interactions", "hoverData")
)
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output("click-data", "children"), Input("basic-interactions", "clickData")
)
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(
    Output("selected-data", "children"), Input("basic-interactions", "selectedData")
)
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@app.callback(
    Output("relayout-data", "children"), Input("basic-interactions", "relayoutData")
)
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)


@app.callback(
    Output("graph1", "figure"),
    Input("comparison", "value"),
)
def update_figure(comparison):

    if comparison == 0:

        overview_df = gfk_df_data.groupby(['buyer']).mean().sort_values(by='buyer', ascending=False)

        fig1 = px.bar(overview_df, y="purchases_per_buyer")
        fig1.update_traces(marker_color=[red, red, red])

    else:

        general_df = gfk_df_data.sort_values(by='buyer', ascending=False)

        fig1 = px.bar(general_df, x="buyer", y="purchases_per_buyer", color='medium', barmode='group',
                        color_discrete_map={
                            'analog': light_red,
                            'digital': dark_red,
                        })

    fig1.update_layout(title='Kaufverhalten',
                        title_font_size=25,
                        xaxis_title='Art der Käufer*innen',
                        yaxis_title='Durchschnittl. Anzahl an Büchern',
                        font_family='Gravitas One',
                        font_color=dark_grey,
                        plot_bgcolor=white,
                        legend_title_text='Art des Buchs'
                    )

    fig1.update_xaxes(fixedrange=True, linecolor=grey, dtick=1)
    fig1.update_yaxes(tick0=0, ticks='inside', range=[0,1], tickcolor=grey, linecolor=grey)

    return fig1


if __name__ == "__main__":
    app.run_server(debug=True)
"""

print('_')

