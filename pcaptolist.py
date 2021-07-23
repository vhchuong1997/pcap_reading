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
# res = ''
    time_list=[]
    frlen_list=[]
    source_list=[]
    des_list=[]
    dur_list=[]
    type_list=[]
    pipe = Popen(tshark_path+" -r "+ input_file + " -T tabs", stdout=PIPE)
    text = pipe.communicate()[0]
    # print(text)
    lists = str(text,'utf-8').split('\r\n')
    a = 0
    for i in lists:
        # print(i)
        a += 1
        temp =  i.strip().split('\t')
        # print(len(temp))
        if len(temp) > 7:
            time = float(temp[1].strip())
            source = temp[2].strip()
            if source == "":
                source = "-"
            destination = temp[4].strip()
            if destination == "":
                destination = "-"
            # protocol = temp[5].strip()
            fr_len = float(temp[6].strip())
            # info = " ".join(temp[7:])
            
            duration = temp[9].strip()
            if duration == "":
                duration = 0
            else: 
                duration = float(duration)

            fr_type = temp[10].strip()
            time_list.append(time)
            frlen_list.append(fr_len)
            source_list.append(source)
            des_list.append(destination)
            dur_list.append(duration)
            type_list.append(fr_type)

            line = '\t'.join((time,source,destination,fr_len,duration,fr_type))
            res = res + '\n' + line
            
            # res.append(el)
            # if a == 1000:
            #     break
    return res

tshark_path = tshark.get_tshark_path()
print(tshark_path)
if (tshark_path == 0):
        print("tshark not found. Please install Wireshark.")

res = pcaptolist( tshark_path,'broadcom.pcap')
# print(res)
text_file = open("result1.txt", "w")
n = text_file.write(res)
text_file.close()
