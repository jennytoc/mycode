farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
ne_animals = farms[0]["agriculture"]
for animal in ne_animals:
    print(animal)

user_input = input("Choose a farm: \n 1. NE Farm \n 2. W Farm \n 3. SE Farm \n")
farm_animals = ""
for farm in farms:
    match user_input:
        case "1":
            farm_animals=farms[0]['agriculture']
            break
        case "2":
            farm_animals=farms[1]['agriculture']
            break
        case "3":
            farm_animals=farms[2]['agriculture']
            break
for animal in farm_animals:
    print(animal)
