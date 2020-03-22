# class Query:
#     def __init__(self):
#         print("Preprocessing")
        
def findDocsByQuery(query, indexs):
    words = query.split(' ')
    s = {}
    no = 1
    for word in words:
        s[word] = indexs[word]
        print(word, "(s",no,"): ", indexs[word])
    print('')
    return s
    
def RetrieveAndLogic(s, docs):
    print("Retrieved object (R) with AND logic")
    if len(s)>1:
        keys   = list(s.keys());
        result = set(s[keys[0]])
        for i in range(len(keys)):
            result = result.intersection(set(s[keys[i]]))

        for item in result:
            print("obj ",item," : ", docs[item-1])
        print('')
        return result
    else:
        print("need more element of s")
    print('')

def RetrieveOrLogic(s, docs):
    print("Retrieved object (R) with OR logic")
    if len(s)>1:
        result = set()
        for item in s.values():
            for col in item:
                result.add(col)
        for item in result:
            print("obj ",item," : ", docs[item-1])
        print('')
        return result
    else:
        print("need more element of s")

def RetrieveNotLogic(s, docs):
    print("Retrieved object (R) with AND logic")
    if len(s)>1:
        keys   = list(s.keys());
        result = set(s[keys[0]])
        for i in range(1,len(keys)):
            result = result.symmetric_difference(s[keys[i]])
        for item in result:
            print("obj ",item," : ", docs[item-1])
        print('')
        return result
    else:
         print("need more element of s")