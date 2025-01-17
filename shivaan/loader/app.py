######################################################################################################
#----------------------------------------IMPORTS-----------------------------------------------------#
######################################################################################################

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import time

from dash.dependencies import Input, Output, State

######################################################################################################
#----------------------------------------DATA--------------------------------------------------------#
######################################################################################################


######################################################################################################
#----------------------------------------CSS STYLING-------------------------------------------------#
######################################################################################################

external_stylesheets = ["https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css"]

card_style = {
                "box-shadow": "0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.3)"
             }

######################################################################################################
#----------------------------------------APP LAYOUT--------------------------------------------------#
######################################################################################################

app = dash.Dash(external_stylesheets=external_stylesheets)

app.scripts.config.serve_locally = True

app.title = "Project CCE"

app.layout = dcc.Loading(
    children=[html.Div(
        className="sans-serif",
        children=[
            html.Div(
                children=[
                    html.H1('Project CCE - Customer Journey'),
                    dcc.Tabs(
                        id="tabs",
                        value="tab-1",
                        children=[
                            dcc.Tab(label="Normal Graph", value="tab-1",
                                    style={'backgroundColor': '#f5f5f5'}),
                            dcc.Tab(label="Funky Graph", value="tab-2",
                                    style={'backgroundColor': '#f5f5f5'}),
                        ],
                        colors={
                            "primary": "white",
                            "background": "white",
                            "border": "#d2d2d2",
                        },
                        parent_style=card_style,
                    ),
                    html.Div(
                        children=[
                            dcc.Loading(id='tabs-content',
                                        type='graph', className='pv6')
                        ],
                        className='pa4'
                    ),
                ],
                style={},
            ),
                            
                            
                            
            html.Div(
                className="w-80 center",
                children=[
                    dcc.Loading(id='output-1', color='gold')
                ],
            ),
            html.Div(
                className="w-80 center",
                children=[
                    dcc.Input(
                        className="db center mv4 ph2 pv1", id="input-1", value="Type here!"
                    )
                ],
            ),
        ],
    )], type = 'cube' , fullscreen = True)


######################################################################################################
#----------------------------------------APP CALLBACKS-----------------------------------------------#
######################################################################################################

@app.callback(Output('output-1', 'children'), [Input('input-1', 'value')])
def render_text(value):
    time.sleep(2)
    return html.H1([value], className='tc gold')


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    time.sleep(2)
    if tab == 'tab-1':
        return html.Div(id='loading-1', children=[
            dcc.Graph(
                id='graph-2-tabs',
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                               350, 430, 474, 526, 488, 537, 500, 439],
                            name='Rest of world',
                            marker=go.bar.Marker(
                                color='rgb(55, 83, 109)'
                            )
                        ),
                        go.Bar(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                               299, 340, 403, 549, 499],
                            name='China',
                            marker=go.bar.Marker(
                                color='rgb(26, 118, 255)'
                            )
                        )
                    ],
                    layout=go.Layout(
                        title='US Export of Plastic Scrap',
                        showlegend=True,
                        legend=go.layout.Legend(
                            x=0,
                            y=1.0
                        ),
                        margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                    )
                ),
            )
        ])
    elif tab == 'tab-2':
        return html.Div(id='loading-2', children=[
            dcc.Graph(
                id='graph-1-tabs',
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                               350, 430, 474, 526, 488, 537, 500, 439],
                            name='Rest of world',
                            marker=go.bar.Marker(
                                color='hotpink'
                            )
                        ),
                        go.Bar(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                               299, 340, 403, 549, 499],
                            name='China',
                            marker=go.bar.Marker(
                                color='gold'
                            )
                        )
                    ],
                    layout=go.Layout(
                        title='US Export of Plastic Scrap',
                        showlegend=True,
                        legend=go.layout.Legend(
                            x=0,
                            y=1.0
                        ),
                        margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                    )
                ),
            )
        ])




######################################################################################################
#----------------------------------------APP DEPLOY--------------------------------------------------#
######################################################################################################

if __name__ == "__main__":
    app.run_server(debug=True)
    
    
    
    
