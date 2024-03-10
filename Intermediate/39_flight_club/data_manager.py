import csv
import os.path
import requests

from key import tequila

class DataManager:

    def __init__(self) -> None:
        self.file_name = 'my_flight.csv'
        self.endpoint = "https://api.tequila.kiwi.com"
        self.headers = {'apikey': tequila}
        self.city_from = dict()


    def add_destination(self):
        """Add new destination. Create new file if doesn't exist."""
        new_info = dict()
        new_info['City'] = input("Where do you want to fly? ")
        new_info['Code'] = self.get_code(new_info['City'])
        new_info['Price'] = int(input("What price do you expect? "))

        mode = 'a+' if os.path.isfile(self.file_name) else 'w'
        with open(self.file_name, mode=mode, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=new_info.keys(), delimiter=';')
            if mode == 'w':
                self.home_city()
                writer.writeheader()
                writer.writerow(self.city_from)
                print("File created. Added home city.")
            writer.writerow(new_info)
            print("Add new destination")

    def home_city(self):
        """Get and save home city in first row."""
        self.city_from['City'] = input("Enter home city: ")
        self.city_from['Code'] = self.get_code(self.city_from['City'])
        self.city_from['Price'] = 0

    def get_code(self, city):
        """Get city code."""
        url = f"{self.endpoint}/locations/query"
        # try 
        response = requests.get(url=url, headers=self.headers, params={'term': city})
        city_code = response.json()['locations'][0]['code']
        print(f"Add city code {city_code}")
        return city_code
