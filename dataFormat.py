import random
import re
import os

MAXENT_DIR = 'data/maxent.txt'
FORMAT_DIR = 'format_data/maxent_formated'
TRAIN_DIR = 'data/maxent_train'
TEST_DIR = 'data/maxent_test'

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

def splitData(train, test):
    with open(FORMAT_DIR, "r") as f:
        data = f.read().split('\n')
    train_data = data[:train]
    test_data = data[test:]
    with open(TRAIN_DIR, 'w') as f:
        for s in train_data:
            f.write((s + u'\n'))

    with open(TEST_DIR, 'w') as f:
        for s in test_data:
            f.write((s + u'\n'))

def main():
    oper = -1
    while int(oper) != 0:
        print('**************************************')
        print('Choose one of the following: ')
        print('1 - Format Data')
        print('2 - Split Data')
        print('0 - Exit')
        print('**************************************')
        oper = int(input("Enter your options: "))

        if oper == 0:
            exit()
        elif oper == 1:
            formatFile(False)
        elif oper == 2:
            exit()

if __name__ == "__main__":
    main()
