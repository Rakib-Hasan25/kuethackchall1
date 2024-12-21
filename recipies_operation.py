# Function to write content to a file
from flask import jsonify, request




def write_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write("\n"+content)
            print(f"Content successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage

def store_recipies_text():
    data = request.get_json() # data come as json object
    dict_data = dict(data)
    recipe_title = dict_data['recipe_title']
    cuisine_type = dict_data['cuisine_type']
    taste_profile = dict_data['taste_profile']
    review = dict_data['review']
    preparation_time = dict_data['preparation_time']
    ingredients = dict_data['ingredients']
    filename = "my_fav_recipies.txt"


    content = f"- {recipe_title}, {cuisine_type}, {taste_profile}, {review}, {preparation_time}, {ingredients}."
    write_to_file(filename, content)
    return jsonify({"data":"successfully write this data"}),200  

