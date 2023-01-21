SERVER = "OpenAI"
BASE = ['engine','model']
UrlBase = "https://seekingalpha.com/"
Extension = ["latest-articles","market-news"]
Headers = {'div':{'data-test-id':'post-list'}}
Article = {'div':{'data-test-id':'content-container'}}
Target = {'a':{'data-test-id':'post-list-item-title'}}

EMBEDDING_PARAMS = {'input':'', 'engine':"text-search-ada-doc-001", 'model':'text-search-ada-doc-001'}
QUESTION_PARAMS = {'input':'', 'engine':"text-search-ada-query-001", 'model':'text-search-ada-query-001'}
ANSWER_PARAMS  = {'engine':"text-davinci-002", 'model':'text-davinci-002',"prompt":"","temperature":0.9,"max_tokens":150,"top_p":0.4,"best_of":1,"frequency_penalty":0.2,"presence_penalty":0.2}
HEADERS=[" Answer the question using the following context, and if the answer is not contained within the text below, say I don't know.\n\nContext:\n","""Make a Summary in 300 words using the provided context \n\nContext:\n"""]
CHABOT_PRE = "Hello, I am MarBot. If you don't have time to read the entire article, I've provided a small section from the article for you to ask question. If you would like to read the full article, it can be found here. Please Rember, you are only able to ask me 3 questions."
IMAGE_LINK = "https://img.freepik.com/premium-vector/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector-stock-illustration_100456-34.jpg?w=2000g"

TMP_CONTAINER = {}
QATOKENS = ["\nQ: ", '\nA: ', '\nSummary: ', '?']
DOC_KEYS = ['data','embedding']
ANSWER_KEYS = ['choices','text']
OPTIONS_MODE = ['OpenChatbot','Summary']
COMPARING_KEY = ['Data','Text', 'Embeddings']




MarvinLinks = ["https://www.linkedin.com/in/marvin-garcia-917127184/","https://www.upwork.com/freelancers/~010d2ff47a39cfb4dd"]
GUIDANCE = "This Chatbot is a proof-of-concept that utilizes GPT-3 and lower versions to showcase the capabilities of new technologies. It connects to the financial news website Seeking Alpha and allows users to search for trending news and analysis. The bot offers two options for users - the ability to ask open-ended questions or generate summaries of the articles they select."
ERROR_MESSAGES = ["There was a Connection Error! Please Contact Marvin"]


# Inline-Blocks-display
inline_flex = {'display':'inline-flex'}
block = {'display':'block'}
display_none = {'display':'none'}

# Width & Height
width_100 = {'width':'100%'}
width_40 = {'with':'40%'}
height_100 = {'height':'100%'}


# Words & Margins
margin_right_5 = {'margin-right':'5px'}
margin_10 = {'margin':'10px'}
margin_15 = {'margin':'15px'}
margin_20 = {'margin':'20px'}

# Words
text_alignn_justify = {'text-align':'justify'}
text_alignn_center = {'text-align':'center'}
select_article_font_size = {'font-size':'1.2rm'}


# Other Options
radio_article_options = [{"label": "Latest New", "value": 'latest-articles'},{"label": "Market News", "value": 'market-news'}]
radio_mode_options = [{"label": "Smart  Summary", "value": 'Summary'},{"label": "Open Questions", "value": 'OpenChatbot'}]

# Div Style
divoption_style = {'min-width':'35%','width':'35%'}
divmid_style = {'display':'inline-flex','width':'100%'}
divchatbot_style = {"height": "100%","padding": "7px","border-style": "groove","border-radius": "5px","display": "flex"}
divimg_style = {"height": "100px","width":"100px","border-radius": "5px"}
divuser_reponse = {'display':'flex', 'margin-top':'5px'}
divcard_body = {'font-size': '1.23rem','font-weight': '300'}