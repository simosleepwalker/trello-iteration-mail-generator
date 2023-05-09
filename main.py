import os

from trello.infrastracture.TrelloApi import TrelloApi
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')

if __name__ == '__main__':
    trelloApi = TrelloApi(API_KEY, API_TOKEN)
    trelloApi.get_board("609b986b54a80584e033ea7d")
