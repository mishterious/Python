# students = [
#      {'first_name':  'Michael', 'last_name': 'Jordan'},
#      {'first_name': 'John', 'last_name': 'Rosales'},
#      {'first_name': 'Mark', 'last_name': 'Guillen'},
#      {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# for i in students:
#     print i['first_name'] + " " + i['last_name']


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
}

for userGroup, userList in users.items(): 
    print userGroup
    for y in userList:
        first = y['first_name']
        last = y['last_name']
        add = len(y['first_name'])+len(y['last_name'])
        userIndex = userList.index(y)+1
        print "{} - {} {} - {}".format(userIndex, first, last, add)

