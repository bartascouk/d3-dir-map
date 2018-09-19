lines = open("dirs.log", "r")


data = []

for line in lines:
    values = line.split("/")
    values.pop(0)
    values[len(values)-1] = values[len(values)-1][:-1] 
    data.append(values)
lines.close()    

print(data)     