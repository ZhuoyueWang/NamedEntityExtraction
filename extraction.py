import re

'''
“January 15, 2014", "the 21st of December", "01/15/2014" (only the American notation),
"Monday", "Monday the 23rd", “Christmas", "Labor Day".
'''



def textRead(inputName):
    textFile = open(inputName,'r')
    lines = textFile.readlines()
    textFile.close()
    for line in lines:
        line = line.lower()
    return lines


def check(lines):
    p1 = re.compile(r'([0-3]\d)?(\s|\/)?((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)|((1[0-2])|(0\d))|(january|february|march|april|may|june|july|august|september|october|november|december))?(\s|\/)\d{4}?')
    #21 jan 2018 | 02 2017 | jan 2017 | 20 12 2017 | 01/15/2014

    p2 = re.compile(r'((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)|((1[0-2])|(0\d))|(january|february|march|april|may|june|july|august|september|october|november|december))?(\s|\/)?([0-3]\d)?(\s|\/)\d{4}?')
    #21 jan 2018 | 02 2017 | jan 2017 | 20 12 2017 |
    p3 = re.compile(r'((monday|tuesday|wednesday|thursday|friday|saturday|friday)|(mon|tue|wed|thu|fri|sat|sun))?\s(the\s)?([0-3]\d)?(st|nd|rd)?')
    #monday monday the 23rd
    p4 = re.compile(r'(the\s)?([0-3]\d(st|nd|rd))?\s(of\s)?(january|february|march|april|may|june|july|august|september|october|november|december)')
    #the 21st of December
    p5 = re.compile(r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)')
    # jan january
    p6 = re.compile(r'(monday|tuesday|wednesday|thursday|friday|saturday|friday|mon|tue|wed|thu|fri|sat|sun)')
    # monday mon
    holidays = ["new year's day", "martin luther king day", "easter", "mother's day", "memorial day", "father's day", "independence day",
    "labor day", "columbus day", "halloween", "veterans day", "thanksgiving day", "christmas" ]

    patternList = [p1, p2, p3, p4, p5, p6, holidays]
    result = list()

    for line in lines:
        for pattern in patternList:
            temp = re.findall(pattern,line)
            if temp != []:
                for elem in temp:
                    result.append(elem)
    return result



def main():
    lines = textRead()
    result = check(lines)
    for i in result:
        print("{}\n".format(i))

if __name__ == "__main__":
    main()

'''

'''
