import sys

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },

    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },

    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
    "starving_bread": {
        "ingredients": ["bread", "cornyflower", "tomatoes"],
        "meal": "lunch",
        "prep_time": 2,
        }
}

name = sys.argv[:1]
ingredients = sys.argv[:2]
meal = sys.argv[:-2]
prep_time = sys.argv[:-1]

for key, value in cookbook.items():
    for x in value["ingredients"]:
        print(x)
print(cookbook["sandwich"]["ingredients"][:1])

for recipe, value in cookbook.items():
    print("==============================")
    print("recipe = ", recipe)
    print("==============================")
    for x_key in value:
        print(x_key + ': ', value[x_key])
print("==============================")
print("==============================")

def print_recipe(name):
#    print("Starving_bread\n\nIngredients : ")
#    for x in cookbook["starving_bread"]["ingredients"]:
#        print("- ",x)
#    print("\nA ", cookbook["starving_bread"]["meal"], " to prepare in : ", cookbook["starving_bread"]["prep_time"], " minutes.")
    name = int(user_choice)
    if name == cookbook[key]:
        print(cookbook["name"])
    print_recipe(name)
print("==============================")

def delete_recipe(name):
    """because cornyflower is disgusting"""
    print(cookbook)
    del cookbook[key]
    print(cookbook)
    name = key
delete_recipe(name)

def add_recipe(name="name", ingredients="ingredients", meal="meal", prep_time="prep_time"):
    """the same with eggs"""

    cookbook["name"] = name
    cookbook["ingredients"] = ingredients
    cookbook["meal"] = meal
    cookbook["prep_time"] = prep_time

add_recipe(name)

#cookbook["starving_bread_bis"] = {
#        "ingredients": ["bread", "eggs", "tomatoes"],
#        "meal": "lunch",
#        "prep_time": 2,
#        }
#    print(cookbook)

def print_all():
#    for name, values in cookbook.items():
#        print(name)
    print(cookbook)
print_all()

def manage_cookbook():
    print("Please select an option by typing the corresponding number:")
    print("1. Add a recipe")
    print("2. Delete a recipe")
    print("3. Print a recipe")
    print("4. Print the cookbook")
    print("5. Quit")

    user_choice = input("What do you want to do? : ")
    if int(user_choice) == 1:
        print("Write the name of recipe, then the ingredients, the kind of meal and the time to prepare it plz")
        add_recipe()
    if int(user_choice) == 2:
        print("what recipe do you want to delete?")
        delete_recipe(sys.argv[0])
    if int(user_choice) == 3:
        print("what recipe do you want to display?")
        print_recipe(name)
    if int(user_choice) == 4:
        print_all()
    if int(user_choice) == 5:
        exit("Cookbook closed")
    if int(user_choice) > 5:
        print("you have to select between 1 and 5")
    if user_choice is not user_choice.isdigit():
        print("enter a number")
manage_cookbook()


