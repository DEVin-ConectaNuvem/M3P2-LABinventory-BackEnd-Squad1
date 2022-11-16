from flask_pymongo import PyMongo

mongo = PyMongo()

def exist_key(request_json, list_keys):
  keys_not_have_in_request = []

  for key in list_keys:
    if key in request_json:
      continue
    else:
      keys_not_have_in_request.append(key)

  if len(keys_not_have_in_request) == 0: 
    return request_json

  return {"error":  f"Está faltando o item {keys_not_have_in_request}"}
