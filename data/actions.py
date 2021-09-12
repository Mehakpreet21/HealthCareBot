# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Union
from geopy.geocoders import Nominatim
import csv
import pandas as pd
import geocoder
from rasa_sdk.events import SlotSet, AllSlotsReset
import requests
import json
from random import randint
import datetime
import os
import yaml
import csv
import pickle
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import string
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pickle
from sklearn.metrics import classification_report
names=[]
phones=[]
ages=[]
symptoms=[]
sides=[]
intensities=[]
locations=[]
class ActionForm(FormAction):
    def name(self) -> Text:
        self.sn=0
        return "form_questions"
    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        return ['name','phone','age']#,'patient id'
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Great! You're registered")
        return []
    def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return{
            'name': [self.from_entity(entity='name', intent='form_entry'),
            self.from_text()],
            'age': [self.from_entity(entity='age', intent='form_entry'),
            self.from_text()],
            'phone': [self.from_entity(entity='phone', intent='form_entry'),
            self.from_text()]
        }

class ActionForm(FormAction):
    def name(self) -> Text:
        self.sn=0
        return "doc_form"
    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        return ['doctor']#,'patient id'
    def submit(self, dispatcher: CollectingDispatcher,
    tracker:Tracker, domain: Dict[Text,Any],
    ) -> List[Dict]:

        dispatcher.utter_message(text="Processing..")
        return[]
    def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return{
            'doctor': [self.from_entity(entity='doctor', intent='doc_name'),
            self.from_text()]
        }

class ActionForm(FormAction):
    def name(self) -> Text:
        return "location_form"
    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        return ['location']#,'patient id'
    def submit(self, dispatcher: CollectingDispatcher,
    tracker:Tracker, domain: Dict[Text,Any],
    ) -> List[Dict]:
        location=tracker.get_slot('location')
# dictionary of lists
        action_place_search()
        return[]
    def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return{
            'location': [self.from_entity(entity='location', intent='location_entry'),
            self.from_text()]
        }
class Side(Action):
    def name(self):
        return 'action_side'
    def run(self,dispatcher,tracker,domain):
        symp=tracker.get_slot('symptom')
        buttons = [{'title': 'na', 'payload': '/side{"side":"na"}'},{'title': 'left', 'payload': '/side{"side":"left"}'}, {'title': 'right', 'payload': '/side{"side":"right"}'}, {'title': 'both', 'payload': '/side{"side":"both"}'}]
        dispatcher.utter_message(template='utter_ask_side',buttons=buttons)
        return[]
    def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return{
            'side': [self.from_entity(entity='side', intent='side'),
            self.from_text()]
        }
class  SymptomSearch(Action):
    def name(self):
        return 'symptom_search'
    def run(self,dispatcher,tracker,domain):
        symp=tracker.get_slot('symptom')
        dispatcher.utter_message('Please choose the intensity of discomformt on a scale of 1-10: ')
        buttons = [{'title': "1", 'payload': '/intensity{"intensity":"1"}'}, {'title': "2", 'payload': '/intensity{"intensity":"2"}'}, {'title': "3", 'payload': '/intensity{"intensity":"3"}'}, {'title': "4", 'payload': '/intensity{"intensity":"4"}'},{'title': "5", 'payload': '/intensity{"intensity":"5"}'}, {'title': "6", 'payload': '/intensity{"intensity":"6"}'},{'title': "7", 'payload': '/intensity{"intensity":"7"}'}, {'title': "8", 'payload': '/intensity{"intensity":"8"}'},{'title': "9", 'payload': '/intensity{"intensity":"9"}'}, {'title': "10", 'payload': '/intensity{"intensity":"10"}'}]
        dispatcher.utter_button_template('utter_ask_intensity', buttons, tracker)
        return []

    def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return{
            'intensity': [self.from_entity(entity='intensity', intent='intensity'),
            self.from_text()]
        }
class ActionIntensity(Action):
    def name(self):
        return 'action_intensity'
    def run(self, dispatcher, tracker, domain):
        intense=int(tracker.get_slot('intensity'))
        side=tracker.get_slot('side')
        symp=tracker.get_slot('symptom')
        filename = r'C:\Users\mehak\Desktop\demobot\chatbot_model_4.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        probabilty= pd.DataFrame(loaded_model.predict_proba([symp]), columns=loaded_model.classes_)
        probability_score=probabilty.melt()
        symptom_list=[]
        if intense>8:
            dispatcher.utter_message("Please call 911 for emergencies")
        for i in range(0,3):
                num=probability_score.nlargest(3,'value')['value']
        if max(num)>95:
                num=probability_score.nlargest(3,'value')['variable'].index[i]
                symptom_list.append(probability_score.nlargest(3,'value')['variable'][num])
                buttons = [{'title': symptom_list[0], 'payload': '/picking_specialty'}]
        else:
            for i in range(0,3):
                    num=probability_score.nlargest(3,'value')['variable'].index[i]
                    symptom_list.append(probability_score.nlargest(3,'value')['variable'][num])
            buttons = [{'title': symptom_list[0], 'payload': '/picking_specialty'},{'title': symptom_list[1] , 'payload': '/picking_specialty'},{'title': symptom_list[2] , 'payload': '/picking_specialty'}]
        dispatcher.utter_button_template('utter_ask_spec', buttons, tracker)
class Summarize(Action):
    def name(self) -> Text:
        return 'summarize'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot('name')
        phone=tracker.get_slot('phone')
        age=tracker.get_slot('age')
        symptom=tracker.get_slot('symptom')
        intense=str(tracker.get_slot('intensity'))
        side=tracker.get_slot('side')
        location=tracker.get_slot('location')
        names.append(name)
        phones.append(phone)
        ages.append(age)
        symptoms.append(symptom)
        locations.append(location)
        intensities.append(intense)
        sides.append(side)
        dict = {'Name': names, 'Phone Number': phones, 'Age': ages, 'Symptoms': symptoms, 'Location':locations, 'Intensity of pain':intensities,'Location of Pain':sides}
        df = pd.DataFrame(dict)
        df.to_csv('Patient Data.csv', header=False, index=False)
        dispatcher.utter_message("Here's a summary of the information your doctor will be provided with: \n \tName: "+str(name)+"\n \tAge: "+str(age)+"\n \tPhone: "+str(phone)+"\n \tSymptoms: "+str(symptom)+"\n \tIntensity of pain: "+str(intense)+"\n \tSide of pain (if applicable):"+str(side))


class ActionPlaceSearch(Action):
    def name(self):
        #define the name of the action
        return 'action_place_search'

    def run(self, dispatcher, tracker, domain):
        #retrieve slot values
        query = tracker.get_slot('amenity')
        radius = 200

        #retrieve google api key
        with open("./ga_credentials.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        key = cfg['credentials']['GOOGLE_KEY']

        import requests
        location=tracker.get_slot('location')
        geolocator = Nominatim(user_agent="demobot")
        location = geolocator.geocode(location)
        place = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}'.format(location.latitude, location.longitude, radius, query, key)).json()
        if len(place['results'])==0:
            dispatcher.utter_message("Sorry, I didn't find anything")
            return []#SlotSet('location_match', 'none')
        else:
            for i in place['results']:
                if 'rating' and 'vicinity' in i.keys():
                    name = i['name']
                    rating = i['rating']
                    address = i['vicinity']
                    if i['opening_hours']['open_now']==True:
                        opening_hours = 'open'
                    else:
                        opening_hours = 'closed'
                    break
        speech = "I found a {} called {} based on your specified parameters.".format(query, name)
        dispatcher.utter_message(speech) #send the response back to the user
        return [] #set returned details as slots
    #SlotSet('location_match', 'one'), SlotSet('rating', rating), SlotSet('address', address), SlotSet('opening_hours', opening_hours)
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_check_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number=tracker.get_slot("phone")
        name=tracker.get_slot("name")
        if number in phones:

            dispatcher.utter_message(text="You're already registered")
        else:
            names.append(name)
            dispatcher.utter_message(text="You're added to the list!")
        return []
class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, I don't understand. Could you rephrase that?")

        return []
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
