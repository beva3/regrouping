# recognition face
datab = [
    "allan",
    "daniel",
    "david",
    "douglas",
    "eduardo"
]

def is_included(person):
    return person in datab

def recognition_face(your_face):
    if is_included(your_face):
        return "Welcome " + your_face
    else:
        return "Sorry, I don't know you"

print(recognition_face("daniel"))
print(recognition_face('raphael'))