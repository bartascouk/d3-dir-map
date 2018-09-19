lines = open("dirs.log", "r")

for line in lines:
    values = line.split("/")
    #print('1 ', values[0],'2 ', values[1], '3 ', values[2] )
    print(values)
lines.close()
~                    