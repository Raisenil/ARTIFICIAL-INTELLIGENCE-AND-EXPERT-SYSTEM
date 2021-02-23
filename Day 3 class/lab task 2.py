table={'clean':'move','dirty':'suck'}

def move(location):
    if location =='A':
        return 'Right'
    elif location =='B':
        return 'Left'

def lookup(percept):
    for i in table:
        if i==percept[1]:
            return table[i]

def table_agnet(percept):
    action=lookup(percept)
    if action =='move':
        action=move(percept[0])
    print(action)           

c='y'
while c !='n':
    room_status=input("Enter status(clean/dirty)")
    room_name=input("Enter room name (A/B)")
    percept=[room_name,room_status]
    table_agnet(percept)
    c=input("Continue?(y/n)")
