import os

from trello.infrastracture.TrelloApi import TrelloApi
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')

if __name__ == '__main__':
    trelloApi = TrelloApi(API_KEY, API_TOKEN)
    lists = trelloApi.get_lists_from(TRELLO_BOARD_ID)
