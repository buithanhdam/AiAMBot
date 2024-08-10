import json
import pandas as pd
import os
# from llama_index.experimental.query_engine import PandasQueryEngine
# from llama_index.core.tools import QueryEngineTool, ToolMetadata
# from llama_index.llms.groq import Groq


def read_file(file_path):
  """
  function read file CSV or Excel.

  Args:
    file_path: Path direction to file.

  Returns:
    DataFrame.
  """
  try:
    df = pd.read_excel(file_path)
  except Exception as e:
    try:
      df = pd.read_csv(file_path)
    except Exception as e:
      print(f"Cant read file: {file_path}")
      return None
  
  return df

def process_data_csv(df, file_path):
    file_name = file_path.split('/')[-1]
    column_info = {col: str(df[col].dtype) for col in df.columns}

    first_5_rows = df.head().to_dict(orient='records')
    file_info = {
        "file_name": file_name,
        "column_count": len(df.columns),
        "column_info": column_info,
        "first_5_rows": first_5_rows
    }
    
    return file_info
def process_data_excel(df):
  for sheet_name, data in df.items():
        print(f"Sheet: {sheet_name}")
        data_head = data.head()  # In 5 dòng đầu tiên của mỗi sheet
        print("Cols info:")
        print(data_head.info())

def extract_json(file_info,json_path):
  json_file = os.path.join(json_path)
  if os.path.exists(json_file):
      os.remove(json_file)
      print(f"File {json_file} was successfully deleted.")
  try:
    with open(json_file, 'w', encoding='utf-8') as f:
      json.dump(file_info, f, ensure_ascii=False, indent=4)
      return json_path
  except Exception as e:
    print("Error",e)
    return None

def retrieve_json(json_path):
  json_file = os.path.join(json_path)
  if os.path.exists(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # import sys
    # sys.stdout.reconfigure(encoding='utf-8')
    # print(json.dumps(data, ensure_ascii=False, indent=4))
    return data
    # first_5_rows = data.get('first_5_rows', [])
    # df = pd.DataFrame(first_5_rows)
    # return df
  else:
    print(f"File {json_file} does not exist .")

def tool_process_data(file_path,json_path):
  df = read_file(file_path)
  file_info = process_data_csv(df,file_path)
  json_path = extract_json(file_info,json_path)


def get_path():
  print(os.path.dirname(__file__))