import re

example = "jdh ausdajbs asd_ASD asdA_as asdj_sd"

print (re.findall("[a-z]_", example))