from trello.application.GetAndUpdateSequence import GetAndUpdateSequence
from trello.domain.TrelloCard import TrelloCard
from trello.infrastracture.TrelloApi import TrelloApi
from jinja2 import Environment, PackageLoader, select_autoescape


class GenerateIterationMail:

    def __init__(self, trello_api: TrelloApi, board_id: str, name: str):
        self.trello_api = trello_api
        self.board_id = board_id
        self.name = name
        self.iteration_number = GetAndUpdateSequence().get_and_update()

    def get_iteration_cards(self) -> [TrelloCard]:
        trello_lists = self.trello_api.get_lists_from(board_id=self.board_id)
        review_list = [tl for tl in trello_lists if tl.name == "Review"][0]
        return self.trello_api.get_cards_from(review_list.list_id)

    def generate_email(self) -> str:
        cards = self.get_iteration_cards()

        env = Environment(
            loader=PackageLoader('trello', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('iteration_mail.txt')

        rendered_email = template.render(
            {
                "name": self.name,
                "cards": cards,
                "iteration_number": self.iteration_number
            }
        )



        return rendered_email
