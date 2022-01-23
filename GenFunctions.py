"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


def bayesNetworkGen(filename):
    f = open(filename,'r')
    ### key-> node | value-> parent, CPT, child
    dict = {}

    for line in f:
        if line == '$$\n':
            break

        string = line.split(">>")
        for x in range(len(string)):
            string[x] = string[x].strip()

        node = string[0]

        parentsString = string[1]
        parentsString = parentsString.strip("[").strip("]")
        parentsList = parentsString.split(",")
        for x in range(len(parentsList)):
            parentsList[x] = parentsList[x].strip()
        if parentsList == ['']:
            parentsList = []


        cptString = string[2]
        cptList = cptString.split(" ")
        cptListinInt = []
        for x in range(len(cptList)):
            cptListinInt.append(float(cptList[x]))

        temp=[]
        temp.append(parentsList)
        temp.append(cptListinInt)
        temp.append([])
        dict[node]=temp

    # print(dict)

    for i in dict.keys():
        temp = dict[i][0]
        for j in temp:
            dict[j][2].append(i)

    # print(dict)
    return dict



def markovBlanketGen(dict, node):

    mbSet = set()
    mbSet.add(node)

    for x in dict[node][0]:
        mbSet.add(x)

    temp = dict[node][2]
    for x in temp:
        mbSet.add(x)

    for x in temp:
        for y in dict[x][0]:
            mbSet.add(y)

    return list(mbSet)


def createExpression(qlist, cList):
    res = "P("

    for i in range(len(qlist) - 1):
        res = res + qlist[i] + ", "

    if len(cList) >= 1:
        res = res + qlist[len(qlist)-1] + " | "
    else:
        res = res + qlist[len(qlist)-1]

    for i in range(len(cList)-1):
        res = res + cList[i] + ", "

    if len(cList) >= 1:
        res = res + cList[len(cList)-1] + ")"
    else:
        res = res + ")"

    return res




# bn = bayesNetworkGen("input1.txt")
# print(bn)
# mb = markovBlanketGen(bn,'B')
# print(mb)

# print(createExpression(['A'], []))


