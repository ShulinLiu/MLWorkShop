import KNN
import matplotlib.pyplot as plt
from numpy import *
import operator

dataset = array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
label = ['L','L','L','A','A','A']

inX = [18,90]
print(KNN.classify0(inX,dataset,label,6))
# group, label = KNN.createDataSet()

# print(group)

# print(label)

# inX = [.5,0.0]
# belong = KNN.classify0(inX,group,label,1)
# print(belong)

# dataSetSize = group.shape[0]
# print(dataSetSize,group.shape[1])
# diffMat = tile(inX, (dataSetSize,1)) - group
# print(diffMat)
# sqDiffMat = diffMat**2
# print(sqDiffMat)
# sqDistances = sqDiffMat.sum(axis=1)
# print(sqDistances)
# distances = sqDistances**0.5
# print(distances)
# sortedDistIndicies = distances.argsort()
# print(sortedDistIndicies)     
# classCount={}          
# for i in range(3):
# 	print(i,sortedDistIndicies[i])
# 	voteIlabel = label[sortedDistIndicies[i]]
# 	print(voteIlabel)
# 	classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
# 	print(classCount[voteIlabel])
# sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
# print(sortedClassCount)
# # return sortedClassCount[0][0]