import json
def parse_json(json_string):
  try:
    data=json.loads(json_string)
    return data
except json.JSONDecodeError as e:
print(f"Error parsing JSON: {e}")
return None
json_data='{"name":"Alice","age":30}'
data_dict=parse_json(json_data)
print(f"Parsed data:{data_dict}")
