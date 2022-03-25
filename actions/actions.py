# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
import logging
from typing import Text, Dict, List, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

# from db_connection import SaveClientData

logger = logging.getLogger(__name__)


class ActionGreetUser(Action):
    """
    Greet user for the first time he has opened the bot windows
    """

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]


def extract_metadata_from_tracker(tracker):
    events = tracker.current_state()['events']
    print(events)
    user_events = []
    for e in events:
        if e['event'] == 'user':
            user_events.append(e)

    return user_events[-1]['metadata']


# class dynamicLink(Action):
#     def name(self) -> Text:
#         return "action_link"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
#         Link_faq = "https://volgai.com/service/seo"
#         dispatcher.utter_template("utter_faq", tracker, link=Link_faq)
#
#         return []


class ValidateClientForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        required_slots = ["fname", "lname", "email", "pnumber"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("required_slot", slot_name)]

        return [SlotSet("requested_slot", None)]


class ActionClientDetailsSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any], ) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_confirm",
        #                          fName=tracker.get_slot("fname"),
        #                          lName=tracker.get_slot("lname"),
        #                          pNumber=tracker.get_slot("pnumber")
        #                          )
        # SaveClientData(
        #     fName=tracker.get_slot("fname"),
        #     lName=tracker.get_slot("lname"),
        #     eMail=tracker.get_slot("email"),
        #     pNumber=tracker.get_slot("pnumber")
        # )

        dispatcher.utter_message(template="utter_details_thanks",
                                 fName=tracker.get_slot("fname"),
                                 lName=tracker.get_slot("lname"),
                                 eMail=tracker.get_slot("email"),
                                 pNumber=tracker.get_slot("pnumber")
                                 )

        return []


class ChooseSEOPlans(Action):
    def name(self) -> Text:
        return "action_seo_plans"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any], ) -> List[Dict[Text, Any]]:
        data = [{"label": "Basic SEO Plan", "value": "basic plan"},
                {"label": "Advance SEO Plan", "value": "advance plan"},
                {"label": "Enterprise SEO Plan", "value": "enterprise plan"}]

        message = {"payload": "dropDown", "data": data}

        dispatcher.utter_message(text="We’ve got 3 plans for SEO that will help you rank your website. Please choose "
                                      "which plan you want to opt for:", json_message=message)

        return []


class ActionQuickReply(Action):
    def name(self) -> Text:
        return "action_seo_feature_reply"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = [{"title": "Local SEO", "payload": "local seo"},
                {"title": "National SEO", "payload": "national seo"},
                {"title": "International SEO", "payload": "international seo"}
                ]

        message = {"payload": "quickReplies", "data": data}

        dispatcher.utter_message(text="SEO services:", json_message=message)

        return []


class ActionCollabsible(Action):
    def name(self):
        return "action_seo_faq"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = [{"title": "How long will it take to rank pages in google or other SERP?",
                 "description": "It will take 4 months to rank domain on serp pages."},
                {"title": "What technique is used to rank pages on keywords?",
                 "description": "We use white hat technique."},
                {"title": "Is it mandatory to do SEO?",
                 "description": "Yes."},
                {"title": "Why are prices different for different plan?",
                 "description": "Because the implementation process is different for variant plans."},
                {"title": "Why are prices different for different plan?",
                 "description": "Because the implementation process is different for variant plans."},
                {"title": "Can we select keywords?",
                 "description": "Yes, You can."},
                {"title": "What tools do you use to find keywords?",
                 "description": "ahref & semrush with screaming frog."},
                {"title": "How do I improve my website's relevancy?",
                 "description": "By creating high authority links which increases E-A-T factor."}
                ]

        message = {"payload": "collapsible", "data": data}

        dispatcher.utter_message(text="Some faqs related to SEO:", json_message=message)

        return []


# class ActionReadCSV(Action):
#     def name(self):
#         return "action_readcsv"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         df = pd.read_csv('data.csv')
#
#         for i, j in df.iterrows():
#             dispatcher.utter_message[text=j]


# class LocationAccess(Action):
#     def name(self) -> Text:
#         return "action_location_access"
#
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message = {"payload": "location"}
#
#         dispatcher.utter_message("Sure, please allow me to access your location 🧐", json_message=message)
#
#         return []


# class ActionReceiveName(Action):
#
#     def name(self) -> Text:
#         return "action_receive_name"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your name {text}!")
#         return [SlotSet("name", text)]


class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        fname = tracker.get_slot("fname")
        lname = tracker.get_slot("lname")

        if not fname and lname:
            dispatcher.utter_message(text="I don't know your name.")
        else:
            dispatcher.utter_message(text=f"Your name is {fname} {lname}!")
        return []

# This code is for action fallback confirmation prompt when intent prediction is low:

# class ActionDefaultAskAffirmation(Action):
#    """Asks for an affirmation of the intent if NLU threshold is not met."""
#
#    def name(self):
#        return "action_default_ask_affirmation"
#
#    def __init__(self):
#        self.intent_mappings = {}
#        # read the mapping from a csv and store it in a dictionary
#        with open('intent_mapping.csv', newline='', encoding='utf-8') as file:
#            csv_reader = csv.reader(file)
#            for row in csv_reader:
#                self.intent_mappings[row[0]] = row[1]
#
#    def run(self, dispatcher, tracker, domain):
#        # get the most likely intent
#        last_intent_name = tracker.latest_message['intent']['name']
#
#        # get the prompt for the intent
#        intent_prompt = self.intent_mappings[last_intent_name]
#
#        # Create the affirmation message and add two buttons to it.
#        # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
#        # when the button is clicked.
#        message = "Did you mean '{}'?".format(intent_prompt)
#        buttons = [{'title': 'Yes',
#                    'payload': '/{}'.format(last_intent_name)},
#                   {'title': 'No',
#                    'payload': '/out_of_scope'}]
#        dispatcher.utter_button_message(message, buttons=buttons)
#
#        return []
