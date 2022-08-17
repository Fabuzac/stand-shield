#!/user/bin/env python3
# coding:utf8
import PyPDF2
import argparse

def get_pdf_meta(file_name):
    pdf_file = PyPDF2.PdfFileReader(open(file_name, "rb"))
    doc_info = pdf_file.getDocumentInfo()

    for info in doc_info:
        print("[+] " + info + " " + doc_info[info])

# def get_string(file_name):
#     with open(file_name, "rb") as file:
#         content = file.read()

parser = argparse.ArgumentParser(description="Outil de forensique")
parser.add_argument("-pdf", dest="pdf", help="Chemin du fichier PDF", required=False)
args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)