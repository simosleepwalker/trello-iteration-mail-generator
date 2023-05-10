import json

import requests as requests

from trello.domain.TrelloBoard import TrelloBoard
from trello.domain.TrelloCard import TrelloCard
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

    def get_list(self, list_id: str) -> TrelloList:
        url = str.format("https://api.trello.com/1/lists/{}", list_id)

        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            params=self.parameters
        )

        result = json.loads(response.text)

        return TrelloList(result["id"], result["idBoard"], result["name"])

    def get_cards_from(self, list_id: str) -> [TrelloCard]:
        url = str.format("https://api.trello.com/1/lists/{}/cards", list_id)

        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            params=self.parameters
        )

        result = json.loads(response.text)
        trello_cards = []

        for res in result:
            trello_cards.append(TrelloCard(res["id"], res["idList"], res["name"]))

        return trello_cards
