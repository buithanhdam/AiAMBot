import os
print(os.getcwd())

from Analysis import read_file,path
from Models import llm_model
context = read_file.retrieve_json(path.JSON_PATH)

query ="Analysis my context and answer the name of the data , num columns , columns type, and show the first 5 rows data in a dataframe"

print(llm_model.print_response(llm_model.make_response(context, query)))