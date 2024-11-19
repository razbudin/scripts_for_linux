import os
# import re


def func_ping(st: str):
    myping = ("ping -q -c 2 %s > /dev/null" % st)
    status = os.system(myping)
    return status


def func_range(st: str):
    start, end = st.split("-")
    start_list = _func_split(start)
    end_list = _func_split(end)
    addr_list = []
    for i in range(int(start_list[3]), int(end_list[-1])+1):
        addr_list.append(f"{start_list[0]}.{start_list[1]}.{
                         start_list[2]}.{i}")
    return addr_list


def func_list(st: str):
    addr_list = st.split(",")
    return addr_list


def _func_split(ip_str: str) -> tuple:
    if ip_str.find(".") != -1:
        a, b, c, d = ip_str.split(".")
    else:
        a, b, c = 0, 0, 0
        d = ip_str.strip()
    return a, b, c, d
