import re

example = "AkzholIsCoding"
example = re.sub("([a-z])([A-Z])", r"\1_\2", example)
print(example.lower())