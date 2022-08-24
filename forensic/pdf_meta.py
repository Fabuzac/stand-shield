#!/user/bin/env python3
# coding:utf8
import PyPDF2
import argparse
import exifread
import re

def get_pdf_meta(file_name):
    pdf_file = PyPDF2.PdfFileReader(open(file_name, "rb"))
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print("[+] " + info + " " + doc_info[info])

def get_string(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())

def get_exif(file_name):
    with open(file_name, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print("Aucune metadonnes EXIF.")
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag]))

# ARGUMENT (flag)
parser = argparse.ArgumentParser(description="Forensic Tool")
parser.add_argument("-pdf", dest="pdf", help="show PDF file metadata raw", required=False)
parser.add_argument("-str", dest="str", help="show PDF file metadata in a string", required=False)
parser.add_argument("-exif", dest="exif", help="show IMAGE file metadata / Supported formats: TIFF, JPEG, PNG, Webp, HEIC", required=False)
args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)

if args.str:
    get_string(args.str)

if args.exif:
    get_exif(args.exif)