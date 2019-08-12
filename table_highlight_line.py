import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table as dt
import pandas as pd

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('train.csv')

def create_table(data,selected_row):
    if selected_row == None:
        return html.Div([
            dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            style_cell={'backgroundColor': '#111111','color': '#FFFFFF'},
            )
        ])

    else:
        return html.Div([
            dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            style_cell={'backgroundColor': '#111111','color': '#FFFFFF'},
            style_data_conditional=[{
                "if": {"row_index": selected_row},
                "backgroundColor": "#2800D7",
                'color': 'white'
            }],
            )
        ])

app.layout=html.Div([
    html.H3('Titanic Dataset', id='title', style={'backgroundColor':'#111111',
    'color':'#FFFFFF','textAlign':'center'}),
    html.Div(id = 'table_container', children = [
    dt.DataTable(id='table')], style= {'display': 'block'}), #hide this at first
    dcc.Store(id = 'table_memory')

],style={'backgroundColor':'#111111'})

@app.callback(Output('table_memory','data'),
            [Input('table','selected_cells')])
def return_row(selected_cell):
    return selected_cell

@app.callback(Output('table_container','children'),
            [Input('table_memory','data')])
def return_table(selected_cell):
    if selected_cell is None:
        whole_table = create_table(df, None)
    else:
        selected_row = selected_cell[0]['row']
        whole_table = create_table(df,selected_row)
    return whole_table


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=False)
