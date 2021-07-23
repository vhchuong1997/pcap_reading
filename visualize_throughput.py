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
import pandas as pd
from subprocess import Popen, PIPE
from tshark import tshark
import matplotlib.pyplot as plt


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

            # line = '\t'.join((source,destination,duration,fr_type))
            # res = res + '\n' + line
            
            # res.append(el)
            # if a == 1000:
            #     break

    return source_list, des_list, dur_list, type_list,time_list,frlen_list


tshark_path = tshark.get_tshark_path()
print(tshark_path)
if (tshark_path == 0):
        print("tshark not found. Please install Wireshark.")

source_list, des_list, dur_list, type_list,time_list,frlen_list = pcaptolist( tshark_path,'123.pcap')

# d = {'time':time_list,'frame length':frlen_list,'source':source_list,'destination':des_list,'duration':dur_list,'fr_type':type_list}
d = {'time':time_list,'frame length':frlen_list}
df = pd.DataFrame(data=d)
# df2 = df.iloc[-1:]
final_time = round(df.iloc[-1:]['time'].values[0])
print(final_time)

time_range_list = []
num_packet_list = []

for i in range(1,final_time+1):
    dfi = df.loc[(df['time'] <= i) & (df['time'] >= i-1)]
    time_range_list.append(i-1)
    num_packet_list.append(len(dfi.index))
    del(dfi)

dfi = pd.DataFrame(data={'time':time_range_list, 'throughput':num_packet_list})
dfi.plot(x ='time', y='throughput', kind = 'line')
# dfi.plot(x ='time', y='throughput', drawstyle = 'steps')
plt.xlabel('time')
plt.ylabel('throughput (packets/s)')

plt.show()