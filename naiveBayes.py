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
      ''' print("probability the target is in e: " + str(probOfeClass))
      print("probability the target is in p: " + str(probOfpClass))    
      print("total amount of product: " +  str(totalCount))    
      print ("Amount of p-class product: " + str(pClassCount))
      print("Amount of e-class product: " + str(eClassCount)) '''       

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
        
              '''print("proability " + str(v))'''
          
      return probDict
    

          
def processTrainingData(trainingDataFile):
  lines = []
  probDictList = []
  setData =  getInitialCounts(trainingDataFile)
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
                for (x,y) in probDict.items():
                  """probDict[x] = y/setData"""
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
    setData = getInitialCounts(trainingDataFile);
    newDict = {}
    newList = []
    yesList = []
    yesDict = {}
    prob_e, prob_p, eclass, pclass, totalCount = classifProb
    lines = []
    probDictList = []
    setData =  getInitialCounts(trainingDataFile)
    k = 0
    counting = 0
    listInc = 0
    yesDictList = []
    elementCount = 0
    probabDictList = []
    probabDict = {}
    probDict = getTrainingData(trainingDataFile, k)
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
    a, b, c, d, e = classifications(trainingDataFile)
    x = 0
    pVal = 1
    originalList = processTrainingData("data2")
    setProbability = 0
    yesdicts, nodicts = trainingApplication(trainingDataFile)
    while x < len(singleArgument):
       for dicts in yesdicts:
         pVal *= dictSearch(yesdicts, dicts, singleArgument, x, totalCount)
         x +=1
    setProbabilityyes = pVal * b 
    
    x = 0
    pVal = 1
    originalList = processTrainingData("data2")
    setProbability = 0
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
    return (classif, "Probability Class = p: " + str(setProbabilityyes) + " Probability Class = e : " + str(setProbabilityno) )
  
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