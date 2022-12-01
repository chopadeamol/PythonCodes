try:
    fp = open('sample.txt')
    print("Sample file has been read")
except IOError as e:
    print("Unable to open the file:", e)