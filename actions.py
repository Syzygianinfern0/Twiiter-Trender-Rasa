from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import tweepy

consumer_key = 'WPKbUCLAEuYlf1gEPavI0YQmJ'
consumer_secret = 'Y18jXjayFQmpeeVaiZSyKBwQSUjCI0rmP3O8fvEE5N84Lop3Td'
access_token = '3438102134-1VH2PeR2uijEOxg54YBbULyRJHwKYp8aW8BW4tH'
access_token_secret = 'YrlQdykFPeybRP92qgla3ZZ8qnJDIgaFKgVfdTEu5qjiZ'

"""
https://www.metaweather.com/api/location/search/?query=delhi
"""
class ActionGetTrends(Action):
    def name(self):
        return "action_get_trends"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        url_for_woeid = 'https://www.metaweather.com/api/location/search/?query=' + city

        try:
            request = json.loads(requests.get(url_for_woeid).text)
            woeid = request[0]
            woeid = woeid['woeid']

            trends1 = api.trends_place(woeid)
            data = trends1[0]
            trends = data['trends']
            names = [trend['name'] for trend in trends]
            top_5_names = names[0:4]
            trendsName = ' '.join(top_5_names)
            dispatcher.utter_message(trendsName)

        except tweepy.error.TweepError as err:
            dispatcher.utter_message("Sorry, I don't have access to that.")

        return [SlotSet("location", city)]
