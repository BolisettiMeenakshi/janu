import json
input = '{"name": "Alice", "age": 30}'
#result = input[1:len(input) - 1]
result = json.loads(input)
#result = json.dumps(input)
print(result)
#print(type(result)) #to check the type of resultsadsadsad