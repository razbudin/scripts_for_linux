#!python3.12
import os
import functions
from sys import argv
from tqdm import tqdm


if argv[1][-4:] == ".txt":
    print("with open()")
    with open("sites.txt") as f:
        mysites = f.readlines()
elif argv[1].find("-") != -1:
    ...
elif argv[1].find(",") != -1:
    ...
else:
    mysites = [argv[1]]

list_fine = []
list_down = []

for site in tqdm(mysites):
    mystatus = functions.func_ping(site.strip())
    if mystatus == 0:
        list_fine.append(site.strip() + " is fine")
    else:
        list_down.append("%s IS DOWN!!!" % (site.strip()))

for site in list_fine:
    print(site)

if len(list_down):
    print()
    print("IT's DOWN")
    for site in list_down:
        print(site)

