cities= ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)

stores=["Walmart", "Target", "Ross", "Academy", "Marshalls", "Hottopic", "Hmart", "Costco", "OfficeDepot", "PartyCity"]
print(stores)

cities[0]
print(cities[0], cities [1], cities [2])

four_cities=cities[0:4]
print(four_cities)

cities[0]="San Francisco"
cities[2]="Brooklyn"
cities[-3]="Hollywood"
cities[5]="Tampa"
print(cities)

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0,"Miami")
print(cities)

del cities[4]
cities.pop(-4)
print(cities)

