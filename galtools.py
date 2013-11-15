def opengal(filename= 'e06.gal'):
    """Takes a keyword argument for a filename and forms the gal file into a dictionary.
    """
    gal = open(filename, 'r')
    worklist = gal.readlines()
    gal.close()

    h = worklist.pop(0).split()
    galList = []
    for i in range(len(worklist)):
        galList.append(map(int, worklist[i].split()))
    if galList[-1] == []:
        if galList[-2][1] == 0:
            pass
        else:
            galList.pop(-1)
    galDict = {}
    count = 0
    zeroindexflag = 0 ##should implement some search for a gal file where the index starts at zero
    while galList:
        if zeroindexflag == 0 and galList[0][1] == 0:
            galDict.update({galList[0][0] : []})
            try:
                if galList[1] == []:
                    galList.pop(1)
                    galList.pop(0)
                else:
                    galList.pop(0)
            except IndexError:
                galList.pop(0)
        else:
            galDict.update({galList[0][0] : galList[1]})
            galList.pop(1)
            galList.pop(0)
    return galDict

def histGal(galDict):
    """Takes a dictionary and returns histogram information
    The output key list is the set of the input keys' value lengths
    The output values are keys of the input dictionary.
    """
    workDict = {}
    lenDict = {}
    for i in range(len(galDict)):
        workDict.update({i+1 : len(galDict.values()[i])})
    for i, val in enumerate(workDict.values()):
        if val not in lenDict:
            lenDict[val] = []
        lenDict[val].append(galDict.keys()[i])
    return lenDict

def asymsearch(galDict):
    """Takes a dictionary and returns a tuple containing asymmetry information
    
    The output tuple contains two dictionaries.
    The first dictionary's keys contain their values, but values do not contain their keys.
    The second dictionary's keys omit their values, but values do not omit their keys.
    """
    tdict = {}
    dleng = range(len(galDict))
    dleng.pop(0)
    dleng.append(len(galDict))
    
    for i in dleng:
        tlist = []
        for j in range(len(galDict.get(i))):
            if (i in galDict.get(galDict.get(i)[j])) == False:
                tlist.append(galDict.get(i)[j])
                tdict.update({i : tlist})
    
    contains = tdict
    omits = {}
    tset = set()
    for i in range(len(contains.values())):
        for j in range(len(contains.values()[i])):
            tset.add(contains.values()[i][j])
    for i in range(len(list(tset))):
        omits.update({list(tset)[i] : []})
    for i in omits:
        for j in contains:
            if (i in contains.get(j)) == True:
                omits.get(i).append(j)
    return contains, omits
