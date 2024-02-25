import re

example = "AhghSjdsjAdJdsjAd"

print(re.sub('([a-z])([A-Z])', r'\1 \2', example))