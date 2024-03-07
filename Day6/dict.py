country = input("Enter the country: ")
visits = int(input("Number of visits: ")) 
list_of_cities = eval(input("Number of cities: "))

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

def add_new_country(country_name, num_visits, list_cities):
  new_country = {}
  new_country["country"]= country_name
  new_country["visits"]=num_visits
  new_country["cities"]=list_cities
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")