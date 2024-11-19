import os


def func_ping(st:str):
    myping = ("ping -q -c 1 %s > ./ping.txt" % st)
    status = os.system(myping)
    return status

