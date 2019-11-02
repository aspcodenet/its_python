import os
import datetime
import argparse

parser = argparse.ArgumentParser(description='append')
parser.add_argument("-rows", required=True, type=int, help="This is number of rows to append")
parser.add_argument("file", default=None, type=str, help="Filename")
args = parser.parse_args()

with open(args.file, "a") as myfile:
    for i in range(0,args.rows):
        datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        myfile.write(f"{datum}\n")

