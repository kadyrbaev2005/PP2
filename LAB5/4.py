import re

example = "sj asdg,asdj asld.asl$fdj54"
example = re.sub(",", ":", example)
example = re.sub(" ", ":", example)
example = re.sub("\.", ":", example)

print (example)