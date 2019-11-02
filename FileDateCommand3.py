import os
import argparse

parser = argparse.ArgumentParser(description='DirLister')
parser.add_argument("-d", required=True, type=str, help="This is the directory")
parser.add_argument("-f", default=None, type=str, help="Filter")

args = parser.parse_args()

for filename in os.listdir(args.d):
    if args.f != None:
        if filename.find(args.f) == -1:
            continue
    s = os.path.getsize(args.d + "\\" + filename)
    print(f"{filename} {s} bytes")
