from flask import request


def store():
    data = request.get_json() # data come as json object
    dict_data = dict(data) # convert json to dict object
    value = dict_data['value']
    return value