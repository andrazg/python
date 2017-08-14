# -*- coding: utf-8 -*-
__author__ = 'Andraz Gruden'

"""PROGRAM UNZIPS AND EDITS FILE FOR PROPPER IMPORT TO DATABASE
    ART -> REPORTING TOOL EXPORTS GZIPPED TSV ONLY
	THIS APP WAS MADE AS A WORKAROUND, THE MAIN THING"""

import os
import sys
import csv
import gzip
import ftplib
import datetime
import time


'# CONNECTION TO FTP'
ftp = ftplib.FTP("LINK", "DB USER", "PASSWORD")
ftp.delete("FILEONFTP.csv")
print ("CONNECTION ESTABLISHED")

"#OPENING FIEL TO UPLOADS"
dat2send = open("//PATH TO FILE/FILETOSENDTOFTP.csv", "rb")

"#FILE TRANSFER"
ftp.storbinary("STOR FILETOSENDTOFTP.csv", dat2send)
print("UPLOADING")
for i in range(1, 15):
    time.sleep(1)
    print str(i),
dat2send.close()
ftp.quit()
log.write((str(datetime.datetime.now().time()) + " UPLOAD OK\n"))

print("\nEND PROGRAM")

log.close()
sys.exit(0)
