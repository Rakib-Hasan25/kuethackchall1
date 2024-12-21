from flask import jsonify, request
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv 
load_dotenv()  
import os



def QuestionAnswer():
    data = request.get_json() # data come as json object
    dict_data = dict(data)
    query_text = dict_data['query_text']
    try:
        llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.environ.get('OPENAI_API_KEY')
        )
         
        with open('my_fav_recipies.txt.txt', 'r') as file:
              context_text = file.read() 
        # PROMPT_TEMPLATE = """
        # You are a culinary expert assisting with dish recommendations. Based on the provided context, suggest a list of dishes along with all the essential ingredients required to prepare them.

        # Context: {context}
        #  Question: {query}
        #  Your Suggestions:
        #   """
        PROMPT_TEMPLATE = """
        You are a culinary expert assisting with dish recommendations. Based on the provided context, suggest a list of dishes along with their essential ingredients in JSON format.

         The JSON structure should look like this:
           [
          {"dish_name": "Dish 1", "ingredients": "item1, item2, item3"},
          {"dish_name": "Dish 2", "ingredients": "item4, item5, item6"}
           ]

           Context: {context}
              Question: {query}

       Your Suggestions (in JSON format):
       """
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text,query=query_text)
        print("oke3")
        response_text = llm.invoke(prompt)
        print(response_text.content)
        return jsonify({"data":response_text.content}),200  

    except Exception as e:  
        return jsonify({"error": str(e)}), 500 
