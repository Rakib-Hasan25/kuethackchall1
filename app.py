from flask import Flask, jsonify, request

app= Flask (__name__)

from ingrediant import add_ingredient, get_ingredients, update_ingredient, delete_ingredient
# from flask_cors import CORS

# CORS(app)

# Routes...

# insert operation
@app.route('/ingredients', methods=['POST'])
def addIngredient():
    return add_ingredient()
# Get operation
@app.route('/ingredients', methods=['GET'])
def getIngredient():
    return get_ingredients()
# Update operation
@app.route('/ingredients/<string:name>', methods=['PUT'])
def updateIngredient(name):
    return update_ingredient(name)
# Delete Operation
@app.route('/ingredients/<string:name>', methods=['DELETE'])
def deleteIngredient(name):
    return delete_ingredient(name)

@app.route('/')
def hello_world():
    return 'Hello, World!'






if(__name__=="__main__"):
    app.run(debug=True)