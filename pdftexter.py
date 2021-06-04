# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import os
import time
import ocrmypdf
import PyPDF2
from PyPDF2 import PdfFileReader
#print(time.time()/3600/24/365.25)

#os.listdir()
os.chdir(r'c:\\Testno')
print(os.getcwd())
#os.listdir()
if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr('4979_210419130705_001.pdf', 'demo.pdf')
    
# temp_pdf = open('demo.pdf', 'rb')


# pdfReader = PyPDF2.PdfFileReader(open('demo.pdf', 'rb'))
# pdftext = ""
# for page in range(pdfReader.numPages):
#     pageObj = pdfReader.getPage(page)
#     pdftext += pageObj.extractText().replace('\n','')
    
# print(pdftext)

#pdf_reader = PyPDF2.PdfFileReader(pdf)
# print("Total number of Pages:", pdf_reader.numPages)

# page = pdf_reader.getPage(0)
# print(page.extractText())
# page = pdf_reader.getPage(1)
# print(page.extractText())

#pdf.close()