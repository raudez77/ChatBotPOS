SERVER = "OpenAI"
BASE = ['engine','model']
UrlBase = "https://seekingalpha.com/"
Extension = ["latest-articles","market-news"]
Headers = {'div':{'data-test-id':'post-list'}}
Article = {'div':{'data-test-id':'content-container'}}
Target = {'a':{'data-test-id':'post-list-item-title'}}

EMBEDDING_PARAMS = {'input':'', 'engine':"text-search-ada-doc-001", 'model':'text-search-ada-doc-001'}
QUESTION_PARAMS = {'input':'', 'engine':"text-search-ada-query-001", 'model':'text-search-ada-query-001'}
ANSWER_PARAMS  = {'engine':"text-davinci-002", 'model':'text-davinci-002',"prompt":"","temperature":0.9,"max_tokens":150,"top_p":0.5,"best_of":1,"frequency_penalty":0.7,"presence_penalty":0.5}
HEADERS=["""Answer the question using the provided context, and if the answer is not contained within the text below, say "I don't know."\n\nContext:\n""","""Make a Summary in 300 words using the provided context \n\nContext:\n"""]
CHABOT_PRE = "Hello, I am MarBot. If you don't have time to read the entire article, I've provided a brief summary for you to ask question. If you would like to read the full article, it can be found here. Please Rember, you are only able to ask me 3 questions."
IMAGE_LINK = "https://img.freepik.com/premium-vector/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector-stock-illustration_100456-34.jpg?w=2000g"

TMP_CONTAINER = {}
QATOKENS = ["\nQ:", '\nA: ', '\nSummary: ', ' ?']
DOC_KEYS = ['data','embedding']
ANSWER_KEYS = ['choices','text']
OPTIONS_MODE = ['OpenChatbot','Summary']
COMPARING_KEY = ['Data','Text', 'Embeddings']
