food_prices = {"Chicken":1.59, "Beef":1.99, "Cheese":1.00, "Milk":2.50 } 
print (food_prices)
print(type(food_prices))
print ()

family_age={"Jr": 10, "Silvia":42, "Alejandra":6, "Saul":15}
print(family_age)

print(food_prices["Chicken"])

print (food_prices["Beef"])

print (food_prices["Cheese"])

print (food_prices["Milk"])

print ()

print(family_age["Jr"])

print(family_age["Silvia"])

print (family_age["Alejandra"])

print (family_age["Saul"])
print ()

shoes_inventory={"Jordan 13":1, "Yeezy":8, "Foamposite":10, "Air Max":5, "SB Dunk":20}
print(shoes_inventory)

print(shoes_inventory["SB Dunk"]-2)
print(shoes_inventory["Yeezy"]+1)
print(shoes_inventory["Jordan 13"]+7)
print(shoes_inventory["Yeezy"]+7)
print(shoes_inventory["Foamposite"]+7)
print(shoes_inventory["Air Max"]+7)
print(shoes_inventory["SB Dunk"]+7)
print(shoes_inventory["Jordan 13"]-3)
print(shoes_inventory["Yeezy"]-3)
print(shoes_inventory["Foamposite"]-3)
print(shoes_inventory["Air Max"]-3)
print(shoes_inventory["SB Dunk"]-3)

shoes_inventory["Vans"]=13
shoes_inventory["Converse"]=25
shoes_inventory["Nike"]=4
print(shoes_inventory)

del shoes_inventory["Nike"]
del shoes_inventory["Converse"]
print (shoes_inventory)
