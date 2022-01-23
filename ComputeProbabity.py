"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import copy
from GenFunctions import bayesNetworkGen


def computeProab(bn, ql,cl):
    temp = ""
    for i in ql:
        if i[0] == '~':
            temp = temp + "0"
        else:
            temp = temp + "1"

    x = int(temp,2)
    # print("x--> ",x)
    resList = enumeration_ask(bn,ql,cl)
    # print("reslist final--> ",resList)
    return resList[x]


def enumeration_ask(bn, ql, cl):
    listOfAllVar = list(bn.keys())
    # print(listOfAllVar)
    resList = []
    statusDict = {}
    temp1 = ""
    temp2 = ""

    for i in cl:
        if i[0] == '~':
            statusDict[i[1]] = 0
        else:
            statusDict[i[0]] = 1
    # print(statusDict)
    combination = 2**len(ql)

    for i in range(combination):

        # i=1
        allCombi = dec_to_bin(i,len(ql))
        # print(allCombi)
        # print("allcombi->",len(allCombi))
        for j in range(len(allCombi)):

            if allCombi[j] == '0':
                if ql[j][0] == '~':
                    temp1 = ql[j].replace("~","")
                else:
                    temp1=ql[j]
                statusDict[temp1] = 0
            else:
                if ql[j][0] == '~':
                    temp1 = ql[j].replace("~","")
                else:
                    temp1=ql[j]
                statusDict[temp1] = 1

        # print(i, statusDict)

        resList.append(enumerate_all(bn,statusDict,listOfAllVar))
        # print("reslist->",resList)
        for j in range(len(ql)):
            if ql[j][0] == '~':
                temp2 = ql[j].replace("~", "")
            else:
                temp2 = ql[j]
            del statusDict[temp2]

    return normalizeResult(resList)


def enumerate_all(bn, statusDict, listOfAllVar):
    if len(listOfAllVar) == 0:
        return 1.0

    first = listOfAllVar[0]
    parentsOfFirst = copy.deepcopy(bn[first][0])

    if first in statusDict.keys():
        return extractProbabFromCPT(first, parentsOfFirst, bn, statusDict, len(parentsOfFirst), "") * enumerate_all(bn, statusDict, listOfAllVar[1:])
    else:
        statusDict[first] = 1
        marginalization1 = extractProbabFromCPT(first, parentsOfFirst, bn, statusDict, len(parentsOfFirst), "") * enumerate_all(bn, statusDict, listOfAllVar[1:])
        # print(marginalization1)
        statusDict[first] = 0
        marginalization2 = extractProbabFromCPT(first, parentsOfFirst, bn, statusDict, len(parentsOfFirst), "") * enumerate_all(bn, statusDict, listOfAllVar[1:])
        # print(marginalization2)
        del statusDict[first]
        # print(marginalization)
        return marginalization1 + marginalization2

def extractProbabFromCPT(first, parents, bn, statusDict, lenOfOriginalParents, cptPositon):

    if len(parents) == 0 and len(cptPositon) == 0:
        if statusDict[first] == 1:
            return bn[first][1][0]
        elif statusDict[first] == 0:
            return (1.0 - bn[first][1][0])

    elif len(parents) == 0 and len(cptPositon) > 0:
        tempInDecimal = int(cptPositon,2)

        if statusDict[first] == 1:
            return bn[first][1][tempInDecimal]
        else:
            return (1.0 - bn[first][1][tempInDecimal])

    else:
        temp = parents[0]
        if temp in statusDict.keys():
            if statusDict[temp] == 0:
                return extractProbabFromCPT(first, parents[1:], bn, statusDict, lenOfOriginalParents, cptPositon + "0")
            elif statusDict[temp] == 1:
                return extractProbabFromCPT(first, parents[1:], bn, statusDict, lenOfOriginalParents, cptPositon + "1")
        else:
            marginalization = extractProbabFromCPT(first, parents[1:], bn, statusDict, lenOfOriginalParents, cptPositon + "0")
            marginalization = marginalization + extractProbabFromCPT(first, parents[1:], bn, statusDict, lenOfOriginalParents, cptPositon + "1")

            return marginalization



def normalizeResult(resList):
    sumOfList = 0.0
    for i in range(len(resList)):
        sumOfList += resList[i]
    for i in range(len(resList)):
        resList[i] /= sumOfList
    return resList


def dec_to_bin(num,length):
    x = bin(num).replace("0b","")
    if len(x) == length:
        return x
    else:
        diff = length - len(x)
        for i in range(diff):
            x = "0" + x
        return x




# bn = bayesNetworkGen("input1.txt")
# print(bn)
# enumeration_ask(bn,None,None)

# print(dec_to_bin(6,5))

# enumeration_ask(bn,['A','~B','C'],['G', '~X'])

# x = normalizeResult([0.00059224, 0.0014919])
# for i in x:
#     print("%.20f"%i)

# p = computeProab(bn,['D'],['~A','B','~C','L'])
# print(p)