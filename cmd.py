import argparse

parser = argparse.ArgumentParser(description="Ange -f file")
parser.add_argument("-f",type=str,help="Ange ett filnamn")
parser.add_argument("-antal",type=int,help="Ange antal")
args = parser.parse_args()

print("Du angav som -f")
print(args.f)

print("Du angav som -antal")
print(args.antal)
