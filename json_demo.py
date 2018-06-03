import json

j = json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}])

print(j)

