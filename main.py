import os

from trello.application.GenerateIterationMail import GenerateIterationMail
from trello.infrastracture.TrelloApi import TrelloApi
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    API_TOKEN = os.getenv('API_TOKEN')
    TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
    RECIPIENT_NAME = os.getenv('RECIPIENT_NAME')

    trelloApi = TrelloApi(API_KEY, API_TOKEN)
    mailGenerator = GenerateIterationMail(trelloApi, TRELLO_BOARD_ID, RECIPIENT_NAME)
    mail = mailGenerator.generate_email()
    print(mail)
