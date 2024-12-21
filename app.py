from flask import Flask, jsonify, request

from ingrediant import store
# from flask_cors import CORS


app= Flask (__name__)
# CORS(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/store-ingrediant',methods=['POST'])  
def ingrediant_store():
    
    return store()







if(__name__=="__main__"):
    app.run(debug=True)