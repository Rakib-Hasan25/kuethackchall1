from pymongo import MongoClient
from pydantic import BaseModel, Field

#MongoDB config
client = MongoClient("mongodb+srv://sowravnath:53CSQ48NVpI2kja5@cluster0.ziygn9y.mongodb.net/")
db = client['ingredients_db']
ingredients_collection = db['ingredients']

class IngredientSchema(BaseModel):
    name: str
    quantity: int = Field(ge=0)