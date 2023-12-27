import os
import numpy as np
from os import listdir

def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

def kNNClassify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)
    return sortedClassCount[0][0]

def handwritingTest(trainingDir, testDir):
    hwLabels = []
    trainingFileList = listdir(trainingDir)
    
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector(trainingDir + '/' + fileNameStr)  # 수정된 부분
    
    testFileList = listdir(testDir)
    mTest = len(testFileList)
    for k in range(1, 21):  # k 값을 1부터 20까지 변화시키면서 에러율 출력
        errorCount = 0.0
        for i in range(mTest):
            fileNameStr = testFileList[i]
            fileStr = fileNameStr.split('.')[0]
            classNumStr = int(fileStr.split('_')[0])
            vectorUnderTest = img2vector(testDir + '/' + fileNameStr)
            classifierResult = kNNClassify(vectorUnderTest, trainingMat, np.array(hwLabels), k)
            if classifierResult != classNumStr:
                errorCount += 1.0
        errorRate = (errorCount / float(mTest)) * 100
        print(int(errorRate))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python student20210773.py <트레이닝 데이터 폴더> <테스트 데이터 폴더>")
        sys.exit(1)
    
    trainingDir = sys.argv[1]
    testDir = sys.argv[2]
    
    handwritingTest(trainingDir, testDir)
