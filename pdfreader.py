# -*- coding: utf-8 -*-
# """
# Created on Tue May  4 10:38:36 2021

# @author: LukaKo
# """

# import PyPDF2
# from PyPDF2 import PdfFileReader

# with open('demo.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)

#     # printing first page contents
#     pdf_page = pdf_reader.getPage(0)
#     print(pdf_page.extractText())

#     # reading all the pages content one by one
#     for page_num in range(pdf_reader.numPages):
#         print(page_num)
#         pdf_page = pdf_reader.getPage(page_num)
#         print(pdf_page.extractText())

# import xlsxwriter
import os
import ocrmypdf
import xlwings as xw
from pdfminer import high_level

###############################################

os.chdir(r'c:\\Testno')
print(os.getcwd())
os.listdir() #prebere lokacijo z datotekami
if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr('0797.pdf', 'demo.pdf') #pretvori pdf v "demo.pdf" s dodanim tekstom

# ##############################################
local_pdf_filename = "demo.pdf"
print(local_pdf_filename)
with open('output.txt', 'w+') as f:
    print(local_pdf_filename)
    pages = [0] # just the first page    
    extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
    print(extracted_text)
    f.write(extracted_text)

fajl = open('output.txt', 'r') #to je naš začasni txt file, kamor shrani tekst
# izhod = open('izhod.txt', 'w')
lajne = fajl.readlines()
# izhod.write(lajne[27])
# print(lajne)
wb = xw.Book('Podatkiosredstvih.xlsx') # to je naša podatkovna baza
sht = wb.sheets['Osnovna Sredstva']  # v kater zavihek/sheet pišemo
exceline = str(xw.Range('J1').end('down').address) #lep trik za najti prvo prazno celico po vrsticah dol
exceline = exceline[3:] #dobi referenčno številko
print(exceline)
exceline= int(exceline)+1
stDobav = 'J' + str(exceline) #lokacija celice (stolpec J, vrstica dobljena zgoraj (prva prazna))
datumDobav = 'I' + str(exceline)
referenca = 'L' + str(exceline)
stRefer = lajne[39] #preberi referenčno številko iz teksta v vrstici 39

for i in range(len(lajne)): #pojdi skozi vrstice
    if lajne[i].startswith('PD'): #če smo našli vrstico ki se začne z PD
        print(lajne[i])
        sht.range(stDobav).value=lajne[i] #vpiši v excel sheet številko dobavnice


# sht.range(stDobav).value = lajne[25]
sht.range(datumDobav).value = lajne[28] #prepiši v excel datum dobavnice
sht.range(referenca).value = lajne[41][18:28] #in referenčno
wb.save() #shrani workbook


# outWorkbook = xlsxwriter.Workbook("out.xlsx")
# outSheet = outWorkbook.add_worksheet()
# outSheet.write("A1", "Številka dobavnice")
# outSheet.write("B1", "Datum dobavnice")
# outSheet.write(1, 0, lajne[25])
# outSheet.write(1, 1, lajne[31])
# outWorkbook.close()