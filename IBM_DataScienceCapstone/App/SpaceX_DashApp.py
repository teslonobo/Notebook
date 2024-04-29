# Import required libraries
import pandas as pd
import dash
from dash import dcc,html

from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
launch_sites = spacex_df['Launch Site'].unique()
print(launch_sites)
#print(spacex_df)

# Create a dash application
app = dash.Dash(__name__)

app.title = 'SpaceX Launch Dashboard'

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=[{'label':'All Sites','value':'ALL'},
                                                      {'label':launch_sites[0],'value':launch_sites[0]},
                                                      {'label':launch_sites[1],'value':launch_sites[1]},
                                                      {'label':launch_sites[2],'value':launch_sites[2]},
                                                      {'label':launch_sites[3],'value':launch_sites[3]},
                                                      ],
                                            value='ALL',
                                            placeholder="place holder here",
                                            searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0,max=10000,
                                                value=[min_payload, max_payload],
                                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value')]
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # If 'ALL' is selected in the dropdown, the pie chart should show the total successful launches count for all sites
        fig = px.pie(spacex_df, names='Launch Site', values='class')
    else:
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie(filtered_df, names='class', title=f'Success vs Failed counts for {selected_site}')
       
    return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    # Filter data based on selected site and payload range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) & (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    # Create scatter chart
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
