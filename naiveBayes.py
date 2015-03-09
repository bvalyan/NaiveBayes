'''
Created on Feb 26, 2015

@author: Brandon
'''
newDictList = []
totalCount = 0;
listLength = 0
listCount = 0
listInc = 0
newDict = {}
accuracy = 0

def getInitialCounts(trainingDataFile):
  pClassCount = 0
  eClassCount = 0

  with open(trainingDataFile) as f:
      global totalCount
      for line in f:
          lines = line.split()
          if(lines[0] == 'p'):
            pClassCount +=1;
          elif(lines[0] == 'e'):
            eClassCount +=1;  
      totalCount = pClassCount + eClassCount
      probOfeClass = eClassCount/totalCount
      probOfpClass = pClassCount/totalCount    

  return totalCount
      
def getTrainingData(trainingDataFile, lineCounter): 
      probDict = {}
      lines = [] 
      with open(trainingDataFile) as f:
        for line in f:
          lines.append(line.split())   
        for lists in lines:
              if lists[lineCounter] not in probDict:
                  probDict[lists[lineCounter]] = 1
              elif lists[lineCounter] in probDict:
                  probDict[lists[lineCounter]] += 1
    
      return probDict
  
def processTrainingData(trainingDataFile):
  lines = []
  probDictList = []
  k = 0
  probDict = getTrainingData(trainingDataFile, k)
  with open(trainingDataFile) as f:
        for line in f:
          lines.append(line.split())  
        for lists in lines:
              global listLength
              listLength = len(lists)
              while k < len(lists): 
                probDict = getTrainingData(trainingDataFile, k)
                probDictList.append(probDict)
                k +=1
  return probDictList

def classifications(trainingDataFile):
  pClassCount = 0
  eClassCount = 0
  with open(trainingDataFile) as f:
      for line in f:
          lines = line.split()
          if(lines[0] == 'p'):
            pClassCount +=1;
          elif(lines[0] == 'e'):
            eClassCount +=1;  
      totalCount = float(pClassCount + eClassCount)
      probOfeClass = float(eClassCount/totalCount)
      probOfpClass = float(pClassCount/totalCount)
  return probOfeClass, probOfpClass,eClassCount, pClassCount, totalCount

def probabCount(lists):
  global listInc
  global newDict 
  if lists[listInc] not in newDict:
      newDict[lists[listInc]] = 1
  else:
      newDict[lists[listInc]] += 1 
     
  return newDict

def trainingApplication(trainingDataFile):
    global newDictList
    global newDict
    global listInc
    classifProb = classifications(trainingDataFile)
    newDict = {}
    newList = []
    yesList = []
    prob_e, prob_p, eclass, pclass, totalCount = classifProb
    lines = []
    k = 0
    counting = 0
    listInc = 0
    elementCount = 0
    probabDictList = []
    probabDict = {}
    with open(trainingDataFile) as f:
        for line in f:
          lines.append(line.split())
        for letters in lines:
              if letters[0] == 'p':
                newList.append(letters)
              else:
                yesList.append(letters)
        while elementCount < len(letters):
          for lists in yesList:
            probabDict[counting] = probabCount(lists)
          counting +=1
          newDict = {}
          listInc += 1
          probabDictList.append(probabDict)
          newDict = {}
          elementCount +=1  
        dictList = probabDict.values()
        for dicts in dictList:
          for (k,v) in dicts.items():
            dicts[k] = float(float(v)/ float(len(yesList)))
        yesDictList = dictList
        
        newDictList = []
        counting = 0
        listInc = 0
        elementCount = 0
        probabDictList = []
        probabDict = {}
        while elementCount < len(letters):
          for lists in newList:
            probabDict[counting] = probabCount(lists)
          counting +=1
          newDict = {}
          listInc += 1
          probabDictList.append(probabDict)
          newDict = {}
          elementCount +=1  
        dictList = probabDict.values()
        for dicts in dictList:
          for (k,v) in dicts.items():
            dicts[k] = float(float(v)/ float(len(newList)))
        newDictList = dictList
    return yesDictList, newDictList
  
def inputClassifier(trainingDataFile ,singleArgument):
    """singleArgument = singleArgument.split()"""
    global listLength
    global classEProb
    global classPprob
    global accuracy
    a, b, c, d, e = classifications(trainingDataFile)
    x = 0
    pVal = 1
    yesdicts, nodicts = trainingApplication(trainingDataFile)
    while x < len(singleArgument):
      for dicts in yesdicts:
        pVal *= dictSearch(yesdicts, dicts, singleArgument, x, totalCount)
        x +=1
    setProbabilityyes = pVal * b 
    x = 0
    pVal = 1
    yesdicts, nodicts = trainingApplication(trainingDataFile)
    while x < len(singleArgument):
      for dicts in nodicts:
        pVal *= dictSearch(nodicts, dicts, singleArgument, x, totalCount)
        x +=1
    setProbabilityno = pVal * a 
    
    
    if setProbabilityyes < setProbabilityno:
      classif = "p"
    else:
      classif = "e"
    
    if classif == singleArgument[0]:
      accuracy +=1
    
    
    return (classif, "Probability Class = p: " + str(setProbabilityyes) + " Probability Class = e : " + str(setProbabilityno) + " Accuracy: " + str(accuracy/e))
  
def dictSearch(yesdicts, dicts, singleArgument, x, totalCount):
  global listLength
  global listCount
  probvalue = 1
  for (k,v) in dicts.items():
    if singleArgument[x] == k:
              probvalue = dicts.get(k)
              return probvalue
     
  return 1     
          
def classify(inputDataFile, trainingDataFile):
  with open(inputDataFile) as f:
    for line in f:
          lines = line.split()
          print(inputClassifier(trainingDataFile, lines))
    
    
print(classify("fullData", "data2"))    