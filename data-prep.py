lines = open("dirs.log", "r")


data = []

for line in lines:
  values = line.split("/")
  values.pop(0)
  values[len(values)-1] = values[len(values)-1][:-1] 
  data.append(values)
lines.close()    

jsonData = {"name": "TopFolder", "children": []}


# create a list of unique first line folders
levelOne = []
for d in data:
  levelOne.append(d[0])
# level one hold unique levele one items
# set return unique values form the list but
# the returned value is not a list anymore
# list() converst output from set back to a list
levelOne = list(set(levelOne))
# print(levelOne)

sameParents = []

for l in levelOne:
  # jsonData["children"].append({"name": l, "children": []})
  sameParent = []
  for d in data:
    if d[0] == l:
      sameParent.append(d)
  sameParents.append(sameParent)

levelOne = None 
# print(sameParents)
# print(len(sameParents))

embeddedChildren = []

for i in sameParents:
  tempI = list(i)
  tempI.pop(0)
  i[0] = {"name": i[0][0], "children":tempI}
  i = i[0]
  embeddedChildren.append(i)

sameParents = None
data = embeddedChildren

# print(data)

for i in data:
  for a in i["children"]:
    a.pop(0)

print("======")

for i in data:
  print(i)

# function to amberd children of children
# data is expected to have the following structure
# {'name': 'bc', 'children': [
#   ['.cache'], 
#   ['.cache', 'abrt'], 
#   ['dconf', 'cach']
# ]}
# Expected output is
# {'name': 'bc', 'children': [
#   ['name': '.cache', 'children': [
#     {'name': 'folder1'},
#     {'name': 'folder2'}
#     ]
#   ],
#   ['name': 'dconf', 'children': [
#     {'name': 'folder1'},
#     {'name': 'folder2'}
#     ]
#   ]  
# ]}
# def embedKids(data):
