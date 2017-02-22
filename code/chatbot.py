from cacheit import getCacheData

# keywords for usecase1
case1Words = set(['get', 'fetch', 'give', 'need', 'want', 'provide', 'download', 'upload', 'have'])
# keywords for usecase2
case2Words = set(['store', 'save', 'keep', 'learn', 'giving', 'providing', 'put'])
# keywords for usecase3
case3Words = set(['search', 'lookup', 'find'])

def identifyUseCase(ip):
    ip = ip.lower()
    ipList = ip.split()
    ipSet = set(ipList)
    for w in ipList:
        if w in case2Words:
            return 2
        elif w in case1Words:
            if checkCase3(ipSet, True):
                return 3
            elif checkCase2(ip, w):
                return 2
            return 1
        elif checkCase3(ipSet, False):
            return 3
    return -1

def checkCase3(ipSet, fromCase1):
    global case3Words
    if fromCase1:
        if 'github' in ipSet:
            return True
        else:
            return False
    for w in case3Words:
        if w in ipSet:
            return True
    for w in case1Words:
        if w in ipSet:
            if 'github' in ipSet:
                return True
            else:
                return False
    return False

def checkCase2(ip, case1Word):
    youIndex = ip.find('you')
    iIndex = ip.find('i')
    case1Index = ip.find(case1Word)
    if youIndex > case1Index or (iIndex != -1 and iIndex < case1Index):
        return True
    return False

def getPattern(ip):
    patternList = []
    flag = 0
    ipList = ip.split()
    actionWords = set(['me', 'you', 'for'])
    actionWords |= case1Words | case2Words
    for w in ipList:
        if w in actionWords:
            flag = 1
            patternList = []
            continue
        elif w.find('pattern') != -1 or w.find('template') != -1:
            flag = 0

        if flag == 1:
            patternList.append(w)
    data = getCacheData()
    pattern = ' '.join(patternList)
    pattern = pattern.lower()
    if pattern in data["diffPatterns"]:
        return data["diffPatterns"][str(pattern)]
    else:
        return pattern

# list of languages in which user can upload the pattern
langList = ['java', 'python', 'node', 'nodejs', 'c', 'c++']

def getLanguage(ip):
    ipList = ip.split()
    for w in ipList:
        if w in langList:
            return w
    return 'NA'

def getAvailableLanguages():
    return langList
