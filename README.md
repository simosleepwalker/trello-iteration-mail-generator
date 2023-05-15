# Trello Iteration Mail Generator

This is a simple Python application which uses **Trello API** to generate an iteration approval email.

To make it work, you have to create a *.env* file in your project directory with all the necessary environment variables:

* **API_KEY** = your Trello API key
* **API_TOKEN** = your Trello token
* **TRELLO_BOARD_ID** = your Trello project board id
* **RECIPIENT_NAME** = the name of the recipient of the email

In order to get Trello API Key and Token follow this guide: https://bostinnovation.com/how-to-get-your-trello-api-key-and-token/

The names of the cards to put in iteration will be taken from the *Trello List* named **Review**, so make sure you
have the iteration cards in that list in your Project Board.

The first iteration will be generated with number 1, after that, a file named `iteration_seq.seq` will be generated,
from there you can put the correct iteration number.
This file will be updated for every correct execution of the script.

At this time, the mail is generated only in italian language.
