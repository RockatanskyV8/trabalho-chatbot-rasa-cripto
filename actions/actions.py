# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

import requests

class SubmitCrypto(Action):

    def name(self) -> Text:
        return "action_submit_crypto"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        crypto = tracker.get_slot('crypto')
        result = self.preco(crypto)
        dispatcher.utter_message(result)

        return [ SlotSet('crypto', None) ]

    def preco(self, crypto):
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + crypto + '&vs_currencies=brl'
        result = requests.get(url, headers={"accept": "application/json"}).json()[crypto]['brl']

        return "preço atual da " + crypto + " R$" + str(result)

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
