import glob
import xlsxwriter 

workbook = xlsxwriter.Workbook('Keywords/Vid.xlsx')
worksheet = workbook.add_worksheet() 
  
# Start from the first cell. 
# Rows and columns are zero indexed. 

worksheet.write(0, 0, 'Title')
worksheet.write(0, 1, 'Description')

row = 1

for file_name in glob.glob('text_files/*'):
	for sub in glob.glob(file_name+'/*'):
		file2 = open(sub)
		line = file2.read()
		worksheet.write(row, 0, sub)
		worksheet.write(row, 1, line)
		file2.close()
		row+=1

workbook.close()

import pandas as pd
data = pd.read_excel("Keywords/Vid.xlsx")
data.to_csv("Keywords/Vid.csv", encoding = 'utf-8', index=False)
