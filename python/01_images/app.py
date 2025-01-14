import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Dash app with pure Altair HTML'

app.layout = html.Div([

    ### ADD CONTENT HERE like: html.H1('text'),
    html.H1('This is my first dashboard'),
    html.H2('This is a subtitle'),

    html.H3('Here is an image'),
    html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Unico_Anello.png/1920px-Unico_Anello.png'),

    html.H5('Here is my actual plot:'),
    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='2000',
        width='1800',
        style={'border-width': '0'},

        ################ The magic happens here
        srcDoc=open('chart.html').read()
        ################ The magic happens here
        ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
