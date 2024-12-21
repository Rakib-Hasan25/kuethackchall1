from flask import Flask, jsonify, request


from chatwithbotoperation import QuestionAnswer
from recipies_operation import store_recipies_text
# from flask_cors import CORS
from ingrediant import add_ingredient, get_ingredients, update_ingredient, delete_ingredient

app= Flask (__name__)
# CORS(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/store-recipies-text',methods=['POST'])
def store_recipies_textform():
    return store_recipies_text()


@app.route('/chat-with-bot',methods=['post'])  
def querywithbot():  
    return QuestionAnswer() 


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






if(__name__=="__main__"):
    app.run(debug=True)