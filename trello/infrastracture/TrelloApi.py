import json

import requests as requests

from trello.domain.Board import Board


class TrelloApi:

    def __init__(self, api_key: str, api_token: str):
        self.api_key = api_key
        self.api_token = api_token
        self.parameters = {
            'key': self.api_key,
            'token': self.api_token
        }

    def get_board(self, board_id: str) -> Board:
        url = "https://api.trello.com/1/boards/" + board_id

        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=self.parameters
        )

        result = json.loads(response.text)

        return Board(result["id"], result["name"])
