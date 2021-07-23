#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    pcaptolist
    ~~~~~~~~~~~~~~~~~~~~
    Allow PCAP capture formated to list-of-dictionary for further process.

    See the README file for details.
    :author: Jonathan <m10802821@gapps.ntust.edu.tw>.
    :license: MIT, see LICENSE for details.
"""

import sys
from subprocess import Popen, PIPE
from tshark import tshark


def pcaptolist(tshark_path, input_file):
    res = ''

    pipe = Popen(tshark_path+" -r "+ input_file + " -T tabs", stdout=PIPE)
    text = pipe.communicate()[0]
    # print(text)
    lists = str(text,'utf-8').split('\r\n')
    a = 0
    for i in lists:
        print(i)
        a += 1
        temp =  i.strip().split('\t')
        if len(temp) > 7:
            source = temp[2].strip()
            if source == "":
                source = "-"
            destination = temp[4].strip()
            if destination == "":
                destination = "-"
            # protocol = temp[5].strip()
            # info = " ".join(temp[7:])
            duration = temp[9].strip() 
            fr_type = temp[10].strip()
            # el = {
            #     "source": source,
            #     "destination" : destination,
            #     # "protocol" : protocol,
            #     # "info" : info
            #     ""
            # }
            line = '\t'.join((source,destination,duration,fr_type))
            res = res + '\n' + line
            
            # res.append(el)
            if a == 100:
                break

    return res

tshark_path = tshark.get_tshark_path()
print(tshark_path)
if (tshark_path == 0):
        print("tshark not found. Please install Wireshark.")

res = pcaptolist( tshark_path,'C:/Users/vhchu/Downloads/2STADL2.pcap')
# print(res)
text_file = open("result1.txt", "w")
n = text_file.write(res)
text_file.close()
