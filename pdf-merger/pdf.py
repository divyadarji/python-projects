# import PyPDF2

# with open('dummy.pdf','rb') as file:
#    reader = PyPDF2.PdfReader(file)
#    print(reader.pages(0))

# import PyPDF2

# with open("dummy.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)  # Update the class name to PdfReader
#     # Now you can use the reader object as before
#     number_of_pages = len(reader.pages)
#     page = reader.pages[0]
#     text = page.extract_text()
#     print(text)

import PyPDF2
import sys

inputs = sys.argv[1:]
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    with open('super.pdf', 'wb') as super_pdf:
         merger.write(super_pdf) 
         
pdf_combiner(inputs)