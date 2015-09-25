import random
import re
import os

#Maxent
MAXENT_DIR = 'data/maxent.txt'
MAXENT_FORMAT_DIR = 'data/maxent/maxent_formated'
MAXENT_TRAIN_DIR = 'data/maxent/maxent_train'
MAXENT_TEST_DIR = 'data/maxent/maxent_test'
MAXENT_PART_DIR = 'data/maxent/maxent_part'
MAXENT_MERGE_DIR = 'data/maxent/maxent_merge'
#SVM
SVM_DIR = 'data/svm.txt'
SVM_FORMAT_DIR = 'data/svm/svm_formated'
SVM_TRAIN_DIR = 'data/svm/svm_train'
SVM_TEST_DIR = 'data/svm/svm_test'
SVM_PART_DIR = 'data/svm/svm_part'
SVM_MERGE_DIR = 'data/svm/svm_merge'
SVM_MALE_KEY = 1
SVM_FEMALE_KEY = -1

def formatFile(type):
    if type:
        formatFileType1()
    else:
        formatFileType2()

def formatFileType1():
    content = ''
    with open(MAXENT_DIR, "r") as f:
        lines = f.readlines()
        for line in lines:
            rgx = re.compile("(\w[\w']*\w|\w)")
            line = line.replace("category","")
            test_list = rgx.findall(line)
            content += test_list[0] + "\t"
            for word in test_list:
                if word != test_list[0]:
                    content += word + ','
            content = content[:-1]
            content += "\n"
    print(content)

    if not os.path.isdir('data/maxent'):
        os.makedirs('data/maxent')

    with open(MAXENT_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def formatFileType2():
    content = ''
    with open(MAXENT_DIR, "r") as f:
        lines = f.readlines()
        for line in lines:
            rgx = re.compile("(\w[\w']*\w|\w)")
            line = line.replace("category","")
            test_list = rgx.findall(line)
            firstChar = test_list[0]
            for word in test_list:
                if word != test_list[0]:
                    content += test_list[0] + "\t" + word + "\n"
    print(content)

    if not os.path.isdir('data/maxent'):
        os.makedirs('data/maxent')

    with open(MAXENT_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def formatFileType3():
    #Format data for SVM
    content = ''
    with open(SVM_DIR, "r") as f:
        lines = f.readlines()
        for line in lines:
            test_list = line.split( )
            key = 1
            if test_list[0] == 'male':
                key = SVM_MALE_KEY
            else:
                key = SVM_FEMALE_KEY
            content += str(key) + " "
            textCount = 1
            for word in test_list:
                if word != test_list[0]:
                    content += str(textCount) + ":" + word + ' '
                    textCount += 1
            content += "\n"
            textCount = 1
    print(content)

    if not os.path.isdir('data/svm'):
        os.makedirs('data/svm')

    with open(SVM_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def splitDataPercent(train, test, isMaxent):
    if isMaxent:
        formatDir = MAXENT_FORMAT_DIR
        trainDir = MAXENT_TRAIN_DIR
        testDir = MAXENT_TEST_DIR
    else:
        formatDir = SVM_FORMAT_DIR
        trainDir = SVM_TRAIN_DIR
        testDir = SVM_TEST_DIR

    with open(formatDir, "r") as f:
        data = f.read().split('\n')

    random.shuffle(data)
    countData = len(data)
    print("countData", countData)
    itemTrainNum = round((train * countData)/100)
    print("itemTrainNum", itemTrainNum)
    itemTestNum = countData - itemTrainNum
    print("itemTestNum", itemTestNum)

    train_data = data[:itemTrainNum]
    test_data = data[itemTrainNum:]

    testContent = ''
    trainContent = ''

    with open(trainDir, 'w') as f:
        for s in train_data:
            if s.strip():
                trainContent += s + u'\n'
        if isMaxent:
            trainContent = trainContent.strip()
        f.write(trainContent)

    with open(testDir, 'w') as f:
        for s in test_data:
            if s.strip():
                testContent += s + u'\n'
        if isMaxent:
            testContent = testContent.strip()
        f.write(testContent)

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[ i * length // wanted_parts: (i + 1) * length // wanted_parts]
             for i in range(wanted_parts) ]

def saveDataPartFile(part_list ,partNum, isMaxent):
    if isMaxent:
        partDir = MAXENT_PART_DIR
    else:
        partDir = SVM_PART_DIR

    print("Part Count", len(part_list))
    content = ''
    file_dir = partDir + str(partNum)
    with open(file_dir, 'w') as f:
        for s in part_list:
            if s.strip():
                content += s + u'\n'
        if isMaxent:
            content = content.strip()
        f.write(content)

def splitDataPartNum(num, isMaxent):
    if isMaxent:
        formatDir = MAXENT_FORMAT_DIR
    else:
        formatDir = SVM_FORMAT_DIR

    with open(formatDir, "r") as f:
        data = f.read().split('\n')
    random.shuffle(data)
    countData = len(data)
    print("countData", countData)

    for x in range(0, num):
        saveDataPartFile(split_list(data, num)[x], x, isMaxent)

def mergeList(testNum, rangeNum, isMaxent):
    if isMaxent:
        partDir = MAXENT_PART_DIR
        mergeDir = MAXENT_MERGE_DIR
    else:
        partDir = SVM_PART_DIR
        mergeDir = SVM_MERGE_DIR

    data = []
    for x in range(0, rangeNum):
        if x != testNum:
            print("MergeCount", str(x) + " | " + str(testNum))
            file_dir = partDir + str(x)
            with open(file_dir, "r") as f:
                data += f.read().split('\n')
    print("MergeCount", len(data))

    content = ''
    file_dir = mergeDir + str(testNum)
    with open(file_dir, 'w') as f:
        for s in data:
            if s.strip():
                content += s + u'\n'
        if isMaxent:
            content = content.strip()
        f.write(content)

def main():
    oper = -1
    while int(oper) != 0:
        print('**************************************')
        print('Choose one of the following: ')
        print('1 - Maxent - Format Data')
        print('2 - Maxent - Split Data for Basic Task')
        print('3 - Maxent - Split Data for Intermediate & Advanced Task')
        print('4 - Maxent - Merge Data for Intermediate & Advanced Task')
        print('5 - SVM - Format Data')
        print('6 - SVM - Split Data for Basic Task')
        print('7 - SVM - Split Data for Intermediate & Advanced Task')
        print('8 - SVM - Merge Data for Intermediate & Advanced Task')
        print('0 - Exit')
        print('**************************************')
        oper = int(input("Enter your options: "))

        if oper == 0:
            exit()
        elif oper == 1:
            formatFile(True)
        elif oper == 2:
            splitDataPercent(80,20, True)
        elif oper == 3:
            splitDataPartNum(5, True)
        elif oper == 4:
            for x in range(0, 5):
                mergeList(x,5, True)
        elif oper == 5:
            formatFileType3()
        elif oper == 6:
            splitDataPercent(80,20, False)
        elif oper == 7:
            splitDataPartNum(5, False)
        elif oper == 8:
            for x in range(0, 5):
                mergeList(x,5, False)


if __name__ == "__main__":
    main()