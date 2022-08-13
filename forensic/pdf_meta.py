#!/user/bin/env python3
# coding:utf8

import PyPDF2

pdf_file = PyPDF2.PdfFileReader(open("pdf/ANONOPS_The_Press_Release.pdf", "rb"))

doc_info = pdf_file.getDocumentInfo()

for info in doc_info:
    print("[+] " + info + " " + doc_info[info])