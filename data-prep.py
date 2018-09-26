import json

lines = open("dirs.log", "r")

data = []

for line in lines:
  values = line.split("/")
  values.pop(0)
  values[len(values)-1] = values[len(values)-1].replace('\n', '')
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

sameParents = []
for l in levelOne:
  # jsonData["children"].append({"name": l, "children": []})
  sameParent = []
  for d in data:
    if d[0] == l:
      sameParent.append(d)
  sameParents.append(sameParent)
levelOne = None 

embeddedChildren = []
for i in sameParents:
  tempI = list(i)
  tempI.pop(0)
  i[0] = {"name": i[0][0], "children":tempI}
  i = i[0]
  embeddedChildren.append(i)
sameParents = None

data = embeddedChildren
for i in data:
  for a in i["children"]:
    a.pop(0)

# function to ambed children of children
# retuns an array to insert under children
def embedKids(kidsArray):
  kids = kidsArray
  # print("=====")
  # print(kids)
  l2 = []
  for k in kids:
    # print(k)
    l2.append(k[0])
  l2 = list(set(l2))
  ln2 = []
  for l in l2:
    sameParent = []
    for k in kids:
      if k[0] == l:
        sameParent.append(k)
    # add children key
    l = {'name': l}
    l['children'] = sameParent
    # print(l)
    ln2.append(l)
  # print(l2)
  return (ln2)

# Embed Children for Level 1
for d in data:
  d['children'] = embedKids(d['children'])

# Remove extraneous data
for d in data:
  for k in d['children']:
    k['children'].pop(0)

for d in data:
  # print("for d in data: " + json.dumps(d))
  for k in d['children']: 
    # print(k)
    # k['children'].pop(0)
    for g in k['children']:
      g.pop(0)
      print(g)

# for d in data:
#   for k in d["children"]:
#     k["children"] = embedKids(k['children'])

# for d in data:
#   for k in d['children']:
#     for g in k['children']:
#       g['children'].pop(0)

print("=====")
print(json.dumps(data, indent=2, sort_keys=False))



