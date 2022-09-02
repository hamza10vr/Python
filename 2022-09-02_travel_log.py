travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

def add_new_country(new_country, num_of_visits, visited_cities):
    new_entry = {
        'country': new_country, 
        'visits': num_of_visits, 
        'cities': visited_cities
    }
    c = ''
    travel_log.append(new_entry)
    print(f"You've visited {new_country} {num_of_visits} times.")
    # cit = city for city in visited_cities
    print(f"You've been to {[city for city in visited_cities]} ")


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
