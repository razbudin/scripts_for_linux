#!python3.12
# import os
import functions
from sys import argv
from tqdm import tqdm


# Получение аргумента и выбор действия
if argv[1][-4:] == ".txt":
    with open(argv[1]) as f:
        mysites = f.readlines()
elif argv[1].find("-") != -1:
    mysites = functions.func_range(argv[1])
elif argv[1].find(",") != -1:
    mysites = functions.func_list(argv[1])
else:
    mysites = [argv[1]]

list_fine = []
list_down = []

# Перебор адресов для ping
# и формирование списков list_fine, list_down
for site in tqdm(mysites):
    mystatus = functions.func_ping(site.strip())
    if mystatus == 0:
        list_fine.append(site.strip() + " is fine")
    else:
        list_down.append(site.strip() + " IS DOWN!!!")

# Печатаем удачные ping-и
for site in list_fine:
    print(site)

# Если list_down не пустой
if len(list_down):
    # Печатаем неудачные ping-и
    print()
    print("IT's sites DOWN")
    for site in list_down:
        print(site)
