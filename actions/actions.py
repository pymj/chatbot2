# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link= "http://www.innovateyourself.in/"
        dispatcher.utter_message(text="Hello! your assistant is here")
        print("Link: ",tracker.get_slot('LINK'))
        #print(tracker.latest_message)
        text=tracker.latest_message['text']
        print(text)
        dispatcher.utter_message(response="utter_info", link=Link)
        return []
