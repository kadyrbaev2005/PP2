import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)