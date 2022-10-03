file = open("scores.txt")

def restaurant_rating(file):

    restaurants = {}

    user_restaurant = input("What restaurant do you want to add?")
    user_rating = input("What is the rating from 1 to 5?")

    restaurants[user_restaurant] = user_rating

    for line in file:
        line = line.rstrip("\n")
        key, value = line.split(':')

        restaurants[key] = value

    print(restaurants.items())
    sorted_restaurants = sorted(restaurants.items())
    print(sorted_restaurants)

    for restaurant, rating in sorted_restaurants:
        print(f"{restaurant} is rated at {rating}.")

restaurant_rating(file)