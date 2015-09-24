import random
import re
import os

MAXENT_DIR = 'data/maxent.txt'
FORMAT_DIR = 'format_data/maxent_formated'
TRAIN_DIR = 'data/maxent_train'
TEST_DIR = 'data/maxent_test'
PART_DIR = 'data/maxent_part'
MERGE_DIR = 'data/maxent_merge'

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

    if not os.path.isdir('format_data'):
        os.makedirs('format_data')

    with open(FORMAT_DIR, "w") as file:
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

    if not os.path.isdir('format_data'):
        os.makedirs('format_data')

    with open(FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def splitDataPercent(train, test):
    with open(FORMAT_DIR, "r") as f:
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

    with open(TRAIN_DIR, 'w') as f:
        for s in train_data:
            if s.strip():
                trainContent += s + u'\n'
        trainContent = trainContent.strip()
        f.write(trainContent)

    with open(TEST_DIR, 'w') as f:
        for s in test_data:
            if s.strip():
                testContent += s + u'\n'
        testContent = testContent.strip()
        f.write(testContent)

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[ i * length // wanted_parts: (i + 1) * length // wanted_parts]
             for i in range(wanted_parts) ]

def saveDataPartFile(part_list ,partNum):
    print("Part Count", len(part_list))
    content = ''
    file_dir = PART_DIR + str(partNum)
    with open(file_dir, 'w') as f:
        for s in part_list:
            if s.strip():
                content += s + u'\n'
        content = content.strip()
        f.write(content)

def splitDataPartNum(num):
    with open(FORMAT_DIR, "r") as f:
        data = f.read().split('\n')
    random.shuffle(data)
    countData = len(data)
    print("countData", countData)

    for x in range(0, num):
        saveDataPartFile(split_list(data, num)[x], x)

def mergeList(testNum, rangeNum):
    data = []
    for x in range(0, rangeNum):
        if x != testNum:
            print("MergeCount", str(x) + " | " + str(testNum))
            file_dir = PART_DIR + str(x)
            with open(file_dir, "r") as f:
                data += f.read().split('\n')
    print("MergeCount", len(data))

    content = ''
    file_dir = MERGE_DIR + str(testNum)
    with open(file_dir, 'w') as f:
        for s in data:
            if s.strip():
                content += s + u'\n'
        content = content.strip()
        f.write(content)

def main():
    oper = -1
    while int(oper) != 0:
        print('**************************************')
        print('Choose one of the following: ')
        print('1 - Format Data')
        print('2 - Split Data for Basic Task')
        print('3 - Split Data for Intermediate & Advanced Task')
        print('4 - Merge Data for Intermediate & Advanced Task')
        print('0 - Exit')
        print('**************************************')
        oper = int(input("Enter your options: "))

        if oper == 0:
            exit()
        elif oper == 1:
            formatFile(True)
        elif oper == 2:
            splitDataPercent(80,20)
        elif oper == 3:
            splitDataPartNum(5)
        elif oper == 4:
            for x in range(0, 5):
                mergeList(x,5)


if __name__ == "__main__":
    main()
