from logging import debug
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
from dash_html_components.Br import Br
from dash_html_components.Button import Button
from dash_html_components.P import P

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.H1('XUST QJT 生成器'),
            html.Br(),
            html.P('姓名'),
            dbc.Input(
                id = 'xm',
                type='text',
                maxLength=5,
                style={'width':'300px'}
            ),
            html.P('学号'),
            dbc.Input(
                id ='xh',
                type = 'text',
                style={'width':'300px'}
            ),
            html.P('请假原因'),
            dbc.Input(
                id ='yy',
                type = 'text',
                style={'width':'300px'}
            ),
            html.P('起始时间'),
            dbc.Input(
                id ='qsqm',
                type = 'text',
                style={'width':'300px'}
            ),
            html.P('终止时间'),
            dbc.Input(
                id ='zszm',
                type = 'text',
                style={'width':'300px'}
            ),
            html.P('请假地点'),
            dbc.Input(
                id ='dd',
                type = 'text',
                style={'width':'300px'}
            ),
            html.Br(),
            html.Button('提交'),
            html.Footer('<--power by jaywxl-->')

        ]
    )
)




if __name__ == '__main__':
    app.run_server(debug=True)