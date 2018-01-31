import re

'''
“January 15, 2014", "the 21st of December", "01/15/2014" (only the American notation),
"Monday", "Monday the 23rd", “Christmas", "Labor Day".
'''



def textRead(inputName):
    textFile = open(inputName,'r')
    lines = textFile.readlines()
    textFile.close()
    return lines


def check(lines):
    #21 jan 2018 | 02 2017 | jan 2017 | 20 12 2017 | 01/15/2014
    #jan 21 2018 | 12 2017 | jan 2017 | 20 12 2017
    #monday the 23rd
    #the 21st of December
    # jan | january
    # monday | mon
    # 2018
    #New Year
    result = list()

    for line in lines:
        pp1 = re.findall(r'(\d\d)(\s|\/)(\d\d|\d)(\s|\/)(\d\d\d\d)', line)
        for i in pp1:
            line = line.replace(''.join(i),'')
        pp21 = re.findall(r'(January|February|March|April|May|June|July|August|September|October|November|December|JANURAY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(\s|\, |\. )(\d\d|\d)(\s|\, |\. )(\d\d\d\d)', line)
        for i in pp21:
            line = line.replace(''.join(i),'')
        pp22 = re.findall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(\s|\, |\. )(\d\d|\d)(\s|\, |\. )(\d\d\d\d)', line)
        for i in pp22:
            line = line.replace(''.join(i),'')
        pp23 = re.findall(r'(January|February|March|April|May|June|July|August|September|October|November|December|JANURAY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(\s|\, |\. )(\d\d\d\d)',line)
        for i in pp23:
            line = line.replace(''.join(i),'')
        pp24 = re.findall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(\s|\, |\. )(\d\d\d\d)',line)
        for i in pp24:
            line = line.replace(''.join(i),'')
        pp3 = re.findall(r'((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)|(Mon|Tue|Wed|Thu|Fri|Sat|Sun))\s(the\s)(\d\d|\d)(st|nd|rd|th)', line)
        for i in pp3:
            line = line.replace(''.join(i),'')
        pp4 = re.findall(r'the\s[0-3]\d(st|nd|rd)\sof\s(January|February|March|April|May|June|July|August|September|October|November|December)', line)
        for i in pp4:
            line = line.replace(''.join(i),'')
        pp5 = re.findall(r'(January|February|March|April|May|June|July|August|September|October|November|December|JANURAY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|Jan |Feb |Mar |Apr |May |Jun |Jul |Aug |Sep |Oct |Nov |Dec |JAN |FEB |MAR |APR |MAY |JUN |JUL |AUG |SEP |OCT |NOV |DEC )', line)
        for i in pp5:
            line = line.replace(''.join(i),'')
        pp6 = re.findall(r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon |Tue |Wed |Thu |Fri |Sat |Sun |MON |TUE |WED |THU |FRI |SAT |SUN )', line)
        for i in pp6:
            line = line.replace(''.join(i),'')
        pp7 = re.findall(r'\d{4}', line)
        for i in pp7:
            line = line.replace(''.join(i),'')
        pp8 = re.findall(r'New Year\'s Day|New Year|NEW YEAR|Martin Luther King Day|Easter|Mother\'s Day|Memorial Day|Father\'s Day|Independence Day|Labor Day|Columbus Day|Halloween|HALLOWEEN|Veterans Day|Thanksgiving Day|Thanksgiving|THANKSGIVING|Christmas|CHRISTMAS', line)
        for i in pp8:
            line = line.replace(''.join(i),'')
        temp = [pp1, pp21, pp22, pp23, pp24, pp3, pp4, pp5, pp6, pp7, pp8]
        for i in temp:
            if len(i) != 0:
                for j in i:
                    result.append(''.join(j))

    return result



def main():
    lines = textRead("input.txt")
    result = check(lines)
    outputFile = open('output.txt','w')
    for i in result:
        print("{}".format(i))
        outputFile.write(i)
        outputFile.write('\n')
    outputFile.close()

if __name__ == "__main__":
    main()
