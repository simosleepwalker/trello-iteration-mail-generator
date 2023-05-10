import os

from trello.application.GenerateIterationMail import GenerateIterationMail
from trello.infrastracture.TrelloApi import TrelloApi
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')

if __name__ == '__main__':
    trelloApi = TrelloApi(API_KEY, API_TOKEN)
    genMail = GenerateIterationMail(trelloApi, TRELLO_BOARD_ID)
    print(genMail.generate_email())
