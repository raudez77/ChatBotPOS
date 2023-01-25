import dash
import core
import time
import os 



from Scripts.actions import * 
from dash import html,dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
from dash.exceptions import PreventUpdate



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], prevent_initial_callbacks=True)


# Load OpenAI key 
api_key = os.environ.get('OPENAI_API_KEY')

# Container Nav and Instruction
DivNav = html.Div(children=[

    # Container Nav
    html.Div(dbc.NavbarSimple(brand="MarBot By Marvin G", brand_href=core.MarvinLinks[0],color="dark",dark=True, children = [
        dbc.NavItem(style=core.inline_flex, children =[
            dbc.NavLink("Linkedln", href=core.MarvinLinks[0]),
            dbc.NavLink("Upwork Profile",href =core.MarvinLinks[1])
        ])
    ])),

    # Instructions
    html.Div(className="p-3 bg-light rounded-3", children=[
        html.P(core.GUIDANCE, style=core.text_alignn_center, className="lead"),
        dcc.ConfirmDialog(id='popup',message=core.ERROR_MESSAGES[0]),
        dcc.ConfirmDialog(id='popup-limit',message=core.ERROR_MESSAGES[1])
    ])
])

# Container Options 
DivOption = html.Div(id='div-options', className="p-3 bg-light rounded-3", style=core.divoption_style, children=[

    # Main Accordion
    dbc.Accordion(style=core.width_40, children=[
        
        # Latest-Trend
        dbc.AccordionItem(title = "Step 1. Categories" , style=core.width_100,children =[
            html.Div(style= core.inline_flex,children=[
                html.H4("Options", style=core.margin_15),
                dbc.RadioItems(id="selected-type",style = core.margin_15, options=core.radio_article_options, inline=True)
            ])
        ]),

        # Articles
        dbc.AccordionItem(title="Step 2. Articles", style=core.width_100,children=[
            html.Div(style=core.block, children = [
                html.H4("Select Article", style=core.select_article_font_size),
                dcc.Loading(id='spinner',type="dot", children=[
                    dbc.Select(id="dropdown-article", children=[])
                ])
            ]),
        ]),

        # Chat Mode
        dbc.AccordionItem(title = "Step 3. ChatBot Mode" , style=core.width_100, children =[
            html.Div(style= core.block,children=[
                html.H4("MarBot Modes", style=core.margin_15),
                dbc.RadioItems(id="chatbot-mode",style = core.margin_15, inline=True, options=core.radio_mode_options)
            ])
        ]),
    ]),

    # Warning
    html.Div(style=core.width_100 ,children=[
            dbc.Card(style = core.margin_10,className="card-text",children=[
                dbc.CardBody( style = core.divcard_body, children=[
                    html.P(children=[
                        "If you're experiencing any issues with the website, try reloading the page.",
                        "Please note that this is just a proof of concept and there is a ",
                        html.Code('$50'),
                        " Credit limit for the OpenAI API.",
                        "Once the credit is used, the demo will be shut down."
                    ])
                ])
            ])
        ]),

    # Reset Button 
    html.A(html.Button("Reset", id="reset-button", className="btn btn-danger", style = core.divreset_button ), href="/") 
])

# Message Before Starting
DivChatSum = html.Div(id ="chatbot-container",style=core.width_100,children=[
    
    # ChatBot First Message Introduction
    html.Div(id='card-container', children = [
        dbc.Card(style=core.height_100,className="card-text",children=[
            dbc.CardBody(id='body-container', children=[
                html.H5("Friendly Reminder" , id='reminder', className="card-title"),
                html.P(id='wait', children=["Wait , The Chatbot will ",html.Code( "answer") ," in here."]),
                dcc.Loading(id="CBS-container", type="dot")
            ])
        ])
    ])
])
        
# Middle Container
DivMid = html.Div(id='response', style=core.divmid_style, children=[DivOption,DivChatSum])

# Initiating Connection with SeekingAlpha 
@app.callback(
    [Output('dropdown-article', 'options'),
     Output('popup', 'displayed')],
    [Input('selected-type', 'value')]
)    

# Initiating Connection with SeekingAlpha 
def DownloadingArticles(value):
    """ Connect to SeekingAlpha
    Parameters;
        value: string, Latest new | market news
        
    """
    if value is None:
        raise PreventUpdate
    else:
        tmp_options = []
        core.TMP_CONTAINER = Connect2Seeking(trigger=True)
        
        
        if core.TMP_CONTAINER:
            for name, _ in core.TMP_CONTAINER[value].items():
                tmp_options.append({'label': name, 'value': name})
            time.sleep(2)
            return tmp_options , False
        else:
            time.sleep(2)
            return [] , True

# Loading Chatbot Summary
@app.callback(
    [
        Output('CBS-container','children'),
        Output('reminder','style'),
        Output('wait','style')
    ],
    [
        Input('selected-type', 'value'),
        Input('dropdown-article','value'),
        Input('chatbot-mode', 'value'),
    ]
)

def LoadingChatSpinningSummary(option_, article_ , mode_):
    if any(opt_ is None for opt_ in [article_ , mode_]):
        raise PreventUpdate
    else:

        Link = core.TMP_CONTAINER[option_][article_]
        _, Article_ = GetArticle(option_,article_)
        Article_ = Article_[list(Article_.keys())[0]][0]

        # Open Question Interface
        # Get Answer Step is not here 
        if mode_ == core.OPTIONS_MODE[0]: 

            # Creating Div ChatBot Open Question : CB-A# : Chatbot-answer #
            DivChatBot = html.Div(id='CB-A', children= [

                # ChatBot Article
                html.Div(id='CB-A-article', style=core.divchatbot_style, children = [

                    # Image
                    html.Div(html.Img(src=core.IMAGE_LINK,style=core.divimg_style)),
                    
                    # Message
                    html.Div(children=[
                        core.CHABOT_PRE,
                        html.H6(dbc.NavLink(f"Full Article in Here : {Link}", href=Link)),
                        html.Div(f"{Article_[:1000]}..."),
                        html.H6("Go Ahead ask me a question..!!!", style =core.margin_15),
                        html.Button("Counter", id='counter', style = core.display_none, n_clicks=0)
                    ]),
                ])
            ])

                # ChatBot Submit Question
            DivUserQuestion = html.Div(id='user-question', style=core.divuser_reponse, children = [
                dbc.Input(id='question', placeholder='Type your question in here', type='text', style=core.margin_right_5),
                html.Button("Submit", id="submit-question", className="btn btn-primary ml-2", n_clicks=0)
            ])

            # Chatbot Answer Container : COQ-container : ChatBot Open Question Container
            DivChaBotContainer = html.Div(id='COQ-container', children = [DivChatBot,DivUserQuestion])

            return DivChaBotContainer, core.display_none, core.display_none

        # Summary
        else:

            # Retrieve Summary
            Message, Summary = UserQuestion(option_,article_,mode_, Question = None)

            # Creating Div for summary CB-Summary : Chat Bot Summary
            DivSummary = html.Div(id='CB-Summary', style = core.inline_flex, children = [

                # 1. ChatBot Image
                html.Div(style=core.margin_right_5, children = [html.Img(src=core.IMAGE_LINK,style=core.divimg_style)]),

                # 2. Chatbot Answer
                html.Div(children= [

                    # Head Greetings & Link
                    html.H5("MarBot Says", className="card-title"),
                    html.H6(dbc.NavLink(f"Full Article in Here : {Link}", href=Link)),

                    # Article First 1000 Words
                    html.H5(f"First 1000 Thousand Words - {article_}", className="card-title"),
                    html.Div(f"{Article_[:1000]}... ", style= core.text_alignn_justify),

                    # Head Summary & Summary 
                    html.H5("Smart Summary:", className="card-title",style= core.margin_20),
                    html.Div(Summary,style= core.text_alignn_justify)

                ])   
            ])

            return DivSummary, core.display_none, core.display_none

# Answering Questions
@app.callback(
    [
        Output("CB-A","children"),
        Output("submit-question",'n_clicks'),
        Output("counter",'n_clicks'),
        Output("question","value"),
        Output("popup-limit","displayed")
    ],
    [
        Input ("submit-question",'n_clicks'),
        Input("counter", "n_clicks"),
        Input ("CB-A","children")
    ],
    [
        State('selected-type', 'value'),
        State('dropdown-article','value'),
        State('chatbot-mode', 'value'),
        State("question","value"),
    ]

)
def QuestionAnswering(n_clicks, counter, children,  option_, article_ , mode_, question_):
    """ Validate Question and Connect To OpenAI"""
    

    # Add One click 
    counter += 1

    if n_clicks == 0:
        raise PreventUpdate

    elif counter > 3 :
        return children, n_clicks,counter, None, True
    
    elif (n_clicks == 1) and (counter <= 3):
        
        _, Answer = UserQuestion(option_, article_ , mode_, question_.strip())
        # Answer = "MockUp Answer"

        # Creating ChatBot Response
        DivChatBotAnswerN = html.Div(id=f'CB-A-{counter}', style=core.divchatbot_style, children = [
            # Image
            html.Div(html.Img(src=core.IMAGE_LINK,style=core.divimg_style)),
                    
            # Message
            html.Div(children=[

                # Question
                html.H6("Your Question", style =core.margin_15),
                html.Div(f"{question_.strip()}", style=core.divChatbotAnswer),

                # Chatbot Answer 
                html.H6("Answer", style =core.margin_15),
                html.Div(f"{Answer.strip()}", style=core.divChatbotAnswer),
            ]),
        ])

        children.append(DivChatBotAnswerN)
        n_clicks = 0
        return children, n_clicks, counter, None , False
    

app.layout = html.Div(children=[
    DivNav,
    DivMid])

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run_server(debug=True, host="0.0.0.0", port=port)