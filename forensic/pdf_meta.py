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

def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float

    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

# TO DO: refactor this function (made in hurry)
def get_gps_from_exif(file_name):
    with open(file_name, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print("No latitude/longitude.")
    else:
        latitude = exif.get("GPS GPSLatitude")
        latitude_ref = exif.get("GPS GPSLatitudeRef")
        longitude = exif.get("GPS GPSLongitude")
        longitude_ref = exif.get("GPS GPSLongitudeRef")
        altitude = exif.get("GPS GPSAltitude")
        altitude_ref = exif.get("GPS GPSAltitudeRef")
        
        if latitude and latitude_ref and longitude and longitude_ref:
            lat = _convert_to_degress(latitude)
            long = _convert_to_degress(longitude) 

            if altitude and altitude_ref:
                alt_ = altitude.values[0]
                alt = alt_.num / alt_.den
                if altitude_ref.values[0] == 1:
                    alt = 0 - alt                
            else:
                print("There not altitude data")

            if str(latitude_ref) != "N":
                lat = 0 - lat
            if str(longitude_ref) != "E" :
                long = 0 - long            
            
            # LATITUDE / LONGITUDE
            print("LAT : " + str(lat) + "\nLONG : " + str(long) + "\nALTITUDE : " + str(alt))
            print("http:maps.google.com/maps?q=loc:%s,%s" % (str(lat), str(long)))
            
# ARGUMENT (flag)
parser = argparse.ArgumentParser(description="Forensic Tool")
parser.add_argument("-pdf", dest="pdf", help="show PDF file metadata raw", required=False)
parser.add_argument("-str", dest="str", help="show PDF file metadata in a string", required=False)
parser.add_argument("-exif", dest="exif", help="show IMAGE file metadata / Supported formats: TIFF, JPEG, PNG, Webp, HEIC", required=False)
parser.add_argument("-gps", dest="gps", help="fetch latitude/longitude/altitude from image", required=False)
args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)

if args.str:
    get_string(args.str)

if args.exif:
    get_exif(args.exif)

if args.gps:
    get_gps_from_exif(args.gps)