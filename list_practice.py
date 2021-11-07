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

def print_city(list):
    for el in list:
        print(el)
    return "All cities printed"

def reorganize_list(list):
    # [1,2,3,4,5]
    print(list)
    counter = 0

    while counter < len(list):
        item1 = list[counter]
        item2 = list[counter]

        if len(item1) >= len(item2):
            counter += 1
            continue

        elif counter + 1== len(list) - 1:
            break
        else: 
            list.remove(item1)
            list.append(item1)
            counter += 1
    return list

def sort_list(list):
    return sorted(list)

print(print_city(cities))
print(reorganize_list(cities))
print(sort_list(stores))
