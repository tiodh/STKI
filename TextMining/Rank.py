# class Rank:
#     def __init__(self):
#         print("Rank Class")

def Jaccard(query, docs):
    words = query.split(" ")
    result = {}
    no = 1
    for doc in docs:
        intersect = set(doc).intersection(words)
        union = set(doc).union(words)
        temp = len(intersect)/len(union)
        if temp>0:
            result[no] = float(temp)
            # print(len(intersect)," / ",len(union)," = ",temp)
        no+=1
    finalResult = {}
    for item in sorted(result, reverse=True, key=result.__getitem__):
        finalResult[item] = result[item]
        print("Doc ", item, " => ", result[item])
    return finalResult

def DiceSorensen(query, docs):
    words = query.split(" ")
    result = {}
    no = 1
    for doc in docs:
        intersect = set(doc).intersection(words)
        temp = 2*len(intersect)/(len(words)+len(doc))
        if temp>0:
            result[no] = temp
            # print(2*len(intersect)," / ",(len(words)+len(doc))," = ",temp)
        no+=1
        
    finalResult = {}
    for item in sorted(result, reverse=True, key=result.__getitem__):
        finalResult[item] = result[item]
        print("Doc ", item, " => ", result[item])
    return finalResult

def OverlapSimilarity(query, docs):
    words = query.split(" ")
    result = {}
    no = 1
    for doc in docs:
        s_min = (len(words),len(doc))
        intersect = set(doc).intersection(words)
        temp = len(intersect)/min(s_min)
        if temp>0:
            result[no] = temp
            # print(len(intersect)," / ",min(s_min)," = ",temp)
        no+=1
    finalResult = {}
    for item in sorted(result, reverse=True, key=result.__getitem__):
        finalResult[item] = result[item]
        print("Doc ", item, " => ", result[item])
    return finalResult