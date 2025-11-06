import os
import getpass
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


from langchain.chat_models import init_chat_model

llm = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    temperature=0.7
)

def generate_restaurant_name_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variable=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest only one fency name (only name) for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variable=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return only the menu items as a comma seperated list."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})

    return response


if __name__ == '__main__':
    response = generate_restaurant_name_and_items('Indian')
    print(response)

