f = open('_chat1.txt','r', encoding="utf8").readlines();
users = []
for each in f:
    if(':' in each and '-' in each):
        ind1 = each.find('-')
        ind2 = each.find(':', ind1)
        users.append(each[ind1:ind2])

allusers = list(set(users))
usermsges = {}
for each in allusers:
    if(users.count(each)>5):
        usermsges[each] = users.count(each)
sorted_dict = sorted( ((value, key) for (key,value) in usermsges.items()) , reverse = True)

print(sorted_dict)
