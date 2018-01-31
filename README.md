# NamedEntityExtraction
##  Temporal Named Entity Extraction
### Zhuoyue Wang, zhuoyue2

Input.txt: the input article we want to extract dates
Extraction.py: the program we execute
Output.txt: the file contains date expressions we identified.

How to run:

Be sure in the working directory which contains these files and type "python3 extraction.py" in the terminal. The output will be printed in terminal and also be in "output.txt".

Program Description:

This python program uses regular expression to identify the date expression patterns such as “January 15, 2014", "January 2014", "the 21st of December", "01/15/2014","Monday", "Monday the 23rd", “Christmas", "Labor Day". It only extracts the longest expression to ensure the accuracy.
