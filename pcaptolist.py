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
import getopt

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

def main(argv):

    try:
        # opts is a list of returning key-value pairs, args is the options left after striped
        # the short options 'hi:o:', if an option requires an input, it should be followed by a ":"
        # the long options 'ifile=' is an option that requires an input, followed by a "="
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("pcaptomsc.py -i <inputfile> -o <output_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("pcaptomsc.py -i <inputfile> -o <output_file>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            if arg[-4:] == ".txt":
                print("outputing to ", arg)
                output_file = arg
            else:
                print("image output must use mscgen as format parameter.\n")
                print("please specify the format parameter before output parameter.\n")
        

    tshark_path = tshark.get_tshark_path()
    print(tshark_path)
    if (tshark_path == 0):
            print("tshark not found. Please install Wireshark.")

    res = pcaptolist( tshark_path,inputfile)
    # print(res)
    text_file = open(output_file, "w")
    n = text_file.write(res)
    text_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])

    