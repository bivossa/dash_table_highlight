import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import pandas as pd

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('train.csv')

app.layout=html.Div([
    html.H3('Titanic Dataset', id='title', style={'backgorundColor':'#111111',
    'color':'#FFFFFF','textAlign':'center'}),
    dt.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
    style_cell={'backgroundColor': '#111111','color': '#FFFFFF'},

    )

],style={'backgroundColor':'#111111'})

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
