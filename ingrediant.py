from flask import Flask, jsonify, request
from pydantic import  ValidationError
from db import ingredients_collection, IngredientSchema

# adding ingredent
def add_ingredient():
    data = request.get_json()
    name = data.get('name')
    quantity = data.get('quantity')
    # check validation for name and quantity
    try:
        ingredient = IngredientSchema(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400
    # check if ingredient already exist
    if ingredients_collection.find_one({"name": name}):
        return jsonify({"error": "Ingredient already exists"}), 400
    # jsonify the ingredient
    ingredient = {
        "name" : name,
        "quantity" : quantity
    }
    # insert ingredient
    ingredients_collection.insert_one(ingredient)
    return jsonify({"message": "Ingredient added successfully"}), 201

# get all ingredient
def get_ingredients():
    ingredients = list(ingredients_collection.find({}, {"_id": 0}))
    return jsonify(ingredients), 200

# Update an ingredient
def update_ingredient(name):
    data = request.get_json()
    quantity = data.get('quantity')

    if quantity is None:
        return jsonify({"error": "Quantity is required"}), 400
    
    result = ingredients_collection.update_one({"name": name}, {"$set": {"quantity": quantity}})
    if result.matched_count == 0:
        return jsonify({"error": "Ingredient not found"}), 404

    return jsonify({"message": "Ingredient updated successfully"}), 200

# delete ingredient
def delete_ingredient(name):
    result = ingredients_collection.delete_one({"name": name})

    if result.deleted_count == 0:
        return jsonify({"error": "Ingredient not found"}), 404

    return jsonify({"message": "Ingredient deleted successfully"}), 200