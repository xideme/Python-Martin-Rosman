import json

json_data='{"nimi":"Marina Oleinik","age":18,"on_prillid":true}'
data_=json.loads(json_data)
for id_, data in enumerate(data_):
    print(id_, ": ", data)
for key, value in data_.items():
    print(key,value)

print(data_)

data_1=json.dumps(json_data)
print(data_1)