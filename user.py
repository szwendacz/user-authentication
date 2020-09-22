import json


class User:
    def __init__(self, name):
        self.name = name
        self.quote_of_the_day = self.get_quote()

    def __str__(self):
        return f"How are you {self.name.capitalize()}? Today quote:  {self.quote_of_the_day}"

    def get_quote(self):
        with open("data.json") as file:
            quote = json.load(file)
        data = quote['contents']['quotes']
        dictionary = dict(data[0])
        return dictionary['quote']