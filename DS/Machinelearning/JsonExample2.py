import json  # json library imported
# json data string
person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj.get('person'))
