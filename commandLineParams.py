import argparse


parser = argparse.ArgumentParser(description="Ange -f <file>")

parser.add_argument("-f",type=str, help="Ange ett filnamn")
args = parser.parse_args()

print(args.f)