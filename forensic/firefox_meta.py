#!/user/bin/env python3
# coding:utf8
import argparse
import sqlite3

def get_firefox_history(places_sqlite):
    try:
        connection = sqlite3.connect(places_sqlite)
        cursor = connection.cursor()
        cursor.execute("""
        
        SELECT url, datetime(last_visit_date/1000000, \"unixepoch\")
        FROM moz_places, moz_historyvisits
        WHERE visit_count > 0 and moz_places.id == moz_historyvisits.place_id

        """)

        print(cursor.fetchall())

        for row in cursor:
            url = str(row[0])
            date = str(row[1])
            print("[+] " + url + " " + date)

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