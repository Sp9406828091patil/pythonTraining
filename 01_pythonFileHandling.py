# # read file
# f = open("demofile.txt", 'rt')
# data = f.read()
# print(data)

#using with statement
with open("demofile.txt", 'rt') as f:
    # data = f.read(5)
    # data1 = f.readlines(1)
    # print(data)
    for eachLine in f:
        print(eachLine)
    # print(data1)

f.close()

# ✅ Common file types you can use with open()
# File type	Example	How to handle
# .txt	Plain text	open('file.txt') → read lines as text
# .csv	Comma-separated values	open('file.csv') + csv module
# .json	JSON data	open('file.json') + json.load()
# .xml	XML data	open('file.xml') + xml parser
# .html	HTML	open('file.html') + BeautifulSoup, etc.
# .log	Logs	open('logfile.log')
# Binary files	.jpg, .png, .pdf, .exe	open('file.jpg', 'rb')

import pandas as pd
df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\New.csv')
print(df)