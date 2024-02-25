import re

example = "asj_sdj lsdk_skd skk_a sl_s"

print(re.sub("_(\w)", lambda x: x.group(1).upper(), example))

###.group() returns the part of the string where there was a match