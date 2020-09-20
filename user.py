import json

import requests


class User:
    def __init__(self, name):
        self.name = name
        self.quote_of_the_day = self.get_quote()

    def __str__(self):
        return f"Jak sie dzisiaj masz {self.name.capitalize()}? Cytaj na dzisiaj to:  {self.quote_of_the_day}"

    def get_quote(self):
        with open("data.json") as file:
            quote = json.load(file)
        data = quote['contents']['quotes']
        dictionary = dict(data[0])
        return dictionary['quote']



user = User("Bartek")

user.get_quote()
