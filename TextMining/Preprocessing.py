# class Preprocessing:
#     def __init__(self):
#         print("Preprocessing")
    
def getFileFromCSV(PathFile):
    import csv
    doc = []
    with open(PathFile) as db_file:
        csv_reader = csv.reader(db_file, delimiter=',')
        for row in csv_reader:
            doc.append(row[0])
        #print
    print('%-3s|%-50s' %('No','Document'))
    print('-'*55)
    no = 1
    for item in doc:
        print('%-3s|%-50s' %(no,item))
        no+=1
    print('')
    return doc
    
def getDistinctWords(tokenize_docs):
    words = set()
    for item in tokenize_docs:
        for word in item:
            words.add(word)
    return words
    
def tokenizing(docs):    
    tokenize_docs = []
    for item in docs:
        tokenize_docs.append(item.split(' '))

    #print
    no = 1
    for item in tokenize_docs:
        print('obj ', no, '-> D', no,' = ', item)
        no += 1
    print('')
    return tokenize_docs

def indexingDocs(docs):
    indexs = {}
    tokenize_docs = tokenizing(docs)
    words = getDistinctWords(tokenize_docs)
    for word in words:
        for num in range(len(tokenize_docs)):
            if word in tokenize_docs[num]:
    #           print(word,' found in doc ', num+1)
                if word in indexs.keys():
                    indexs[word].append(num+1)
                else:
                    indexs[word] = [num+1]

    print('%-15s|%-3s' %('Dictionary','Inverted List'))
    print('-'*30)
    for item in sorted(indexs.keys()):
        print('%-15s|%-3s' %(item, indexs[item]))
    print('')
    return indexs