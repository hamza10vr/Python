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




def add_new_country(country_visited, num_of_visits, visited_cities):
    new_entry = {
        'country': country_visited, 
        'visits': num_of_visits, 
        'cities': visited_cities
    }
    ############ METHOD 2 ###############
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = num_of_visits
    new_country['cities'] = visited_cities
    #######################################

    travel_log.append(new_entry)
    print(f"You've visited {country_visited} {num_of_visits} times.")

    cities_visited = ''
    for city in visited_cities:
        cities_visited += city + ' and '
    print(f"You've been to {cities_visited} ")


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
