import os
import sys
directory_in_str=os.path.abspath(sys.argv[1])
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".asm") or filename.endswith(".py"):
        print(os.path.join(directory, filename))
        continue
    else:
        continue