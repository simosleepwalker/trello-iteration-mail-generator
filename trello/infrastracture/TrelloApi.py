import json

import requests as requests

from trello.domain.TrelloBoard import TrelloBoard
from trello.domain.TrelloList import TrelloList


class TrelloApi:

    def __init__(self, api_key: str, api_token: str):
        self.api_key = api_key
        self.api_token = api_token
        self.parameters = {
            'key': self.api_key,
            'token': self.api_token
        }
        self.headers = {
            "Accept": "application/json"
        }

    def get_board(self, board_id: str) -> TrelloBoard:
        url = str.format("https://api.trello.com/1/boards/{}", board_id)

        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            params=self.parameters
        )

        result = json.loads(response.text)

        return TrelloBoard(result["id"], result["name"])

    def get_lists_from(self, board_id: str) -> [TrelloList]:
        url = str.format("https://api.trello.com/1/boards/{}/lists", board_id)

        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            params=self.parameters
        )

        result = json.loads(response.text)
        trello_lists = []

        for res in result:
            trello_lists.append(TrelloList(res["id"], res["idBoard"], res["name"]))

        return trello_lists
