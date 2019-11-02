import os
import datetime
import argparse
import shutil



parser = argparse.ArgumentParser(description='append')
parser.add_argument("-f", required=True, type=str, help="Fil")
parser.add_argument("-d", default=None, type=str, help="Dir")
args = parser.parse_args()

if not os.path.exists(args.d):
    os.makedirs(args.d)

newName = args.d + "\\" + args.f
if os.path.exists(newName):
    datum = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename, file_extension = os.path.splitext(newName)
    newName = filename + datum + file_extension
shutil.copyfile(args.f,newName)
