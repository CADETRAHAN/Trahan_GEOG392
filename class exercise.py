from pathlib import Path
#print(Path.cwd())

path = 'C:/Users/cadet/Devsource/Trahan_GEOG392/geog392.txt'
fileread = open(path, 'r')
myread = fileread.readlines()
for line in myread:
    print(line)
fileread.close()