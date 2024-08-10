from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.core import PromptTemplate
from llama_index.llms.openai import OpenAI
import os
load_dotenv()
################################

def prompt(prompt_tmpl_str,context,query):
    prompt_tmpl = PromptTemplate(prompt_tmpl_str)
    partial_prompt_tmpl = prompt_tmpl.partial_format(tone_name="Shakespeare")

    fmt_prompt = partial_prompt_tmpl.format(
        my_context=context,
        my_query=query
    )
    return fmt_prompt
# print(fmt_prompt)
def model():
    api_key=os.environ['GEMINI_API_KEY']
    gemini_model = Gemini(api_key=api_key,temperature=0.2)
    return gemini_model

def make_response(context,query):
    qa_prompt_tmpl_str = """\
Context information is below.
---------------------
{my_context}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {my_query}
Answer: \
"""
    resp = model().complete(prompt(qa_prompt_tmpl_str,context,query))
    return resp
def print_response(response):
    try:
        # Try to print directly
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
    except UnicodeEncodeError as e:
        print("Error",e)