import re

example = "asjdASHDJjd askjdaJASD sdjaASJD ASKDJasd asdAk AJshda"

print(re.findall("[A-Z][a-z]", example))