spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "N/A")
        cuisine = food.get("cuisine", "N/A")
        heat_level = food.get("heat_level", 0)
        chili_string = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    hottest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(hottest_foods)

def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]

# Sample usage (for testing/demonstration)
if __name__ == "__main__":
    print("Names of spicy foods:")
    print(get_names(spicy_foods))

    print("\nSpiciest foods:")
    print(get_spiciest_foods(spicy_foods))

    print("\nAll spicy foods:")
    print_spicy_foods(spicy_foods)

    print("\nSpicy food by cuisine (Thai):")
    print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

    print("\nPrint only the spiciest foods:")
    print_spiciest_foods(spicy_foods)

    print("\nAverage heat level:")
    print(get_average_heat_level(spicy_foods))

    new_spicy_food = {"name": "Jalapeño Poppers", "cuisine": "Tex-Mex", "heat_level": 4}
    updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
    print("\nUpdated list of spicy foods:")
    print(updated_spicy_foods)
