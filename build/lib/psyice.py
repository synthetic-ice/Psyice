#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os


def printList(lst, indent=False, level=0):
    for each in lst:
        if isinstance(each, list):
            printList(each, indent, level+1)
        else:
            if indent is True:
                for i in range(level):
                    print("\t", end="")
            print(each)
    return None


def modifyMirrorlist(mirrorlist):
    """
        Modify Arch Linux mirrorlist, leaving only Chinese repos
        In order to use it, you should provide a parameter
        (the location of mirrorlist file)
    """
    dataRead = open(mirrorlist)
    urls = []
    findChina = False
    for eachLine in dataRead:
        if (not findChina and eachLine.find("China") != -1):
            findChina = True
        if (findChina):
            if (len(eachLine) != 1):
                urls.append(eachLine)
            else:
                break
    dataRead.close()
    urls.pop(0)
    dataWrite = open(mirrorlist, 'w')
    for each in urls:
        each = each[1:]
        dataWrite.write(each)
    dataWrite.close()
    return None
