#!/user/bin/env python3
# coding:utf8
import argparse
import sqlite3
import htmlFirefox
import os

def get_firefox_history(places_sqlite):
    try:
        connection = sqlite3.connect(places_sqlite)
        cursor = connection.cursor()
        cursor.execute("""
        
        SELECT url, datetime(last_visit_date/1000000, \"unixepoch\")
        FROM moz_places, moz_historyvisits
        WHERE visit_count > 0 and moz_places.id == moz_historyvisits.place_id

        """)        
            
        with open("C:/Users/N9/Desktop/rapport_firefox_history.html", "a") as f:
            f.write(htmlFirefox.header)
            for row in cursor:
                url = str(row[0])
                date = str(row[1])
                f.write("<tr><td><a href='" + url + "'>" + url + "</a></td><td>" + date + "</td></tr>")
            f.write(htmlFirefox.footer)
            print("File history created with success")
            f.close()
    except Exception as error:
        print("[-] Error : " + str(error))
        exit(1)

# ARGUMENT (flag)
parser = argparse.ArgumentParser(description="Forensic Tool")
parser.add_argument("-fh", dest="fhistory", help="fetch firefox history from palces.sqlite file", required=False)
args = parser.parse_args()

if args.fhistory:
    get_firefox_history(args.fhistory)


#         SELECT url, last_visit_day, datetime(last_visit_date/1000000, \"unixepoch\")
#         FROM moz_places, moz_historyvisits
#         WHERE visit_count > 0 and moz_places.id == moz_historyvisits.place_id