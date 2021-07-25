import sys
import pyshark
import pandas as pd
import matplotlib.pyplot as plt
import getopt

def main(argv):
    output_flag = False
    try:
        # opts is a list of returning key-value pairs, args is the options left after striped
        # the short options 'hi:o:', if an option requires an input, it should be followed by a ":"
        # the long options 'ifile=' is an option that requires an input, followed by a "="
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("pyshark_visualize_throughput.py -i <pcap_file_input> -o <csv_file_output>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("pyshark_visualize_throughput.py -i <pcap_file_input> -o <csv_file_output>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            if arg[-4:] == ".csv":
                print("outputing to ", arg)
                output_file = arg
                output_flag = True
            else:
                print("image output must use mscgen as format parameter.\n")
                print("please specify the format parameter before output parameter.\n")


    capture = pyshark.FileCapture(inputfile)

    time_list = []
    frlen_list = []
    for packet in capture:
        time_list.append(float(packet.frame_info.time_relative))
        frlen_list.append(float(packet.length))

    d = {'time':time_list,'frame length':frlen_list}
    df = pd.DataFrame(data=d)

    final_time = round(df.iloc[-1:]['time'].values[0])
    print(final_time)

    time_range_list = []
    num_packet_list = []

    for i in range(final_time):
        dfi = df.loc[(df['time'] <= i+1) & (df['time'] >= i)]
        time_range_list.append(i)
        num_packet_list.append(dfi['frame length'].sum())
        del(dfi)

    dfi = pd.DataFrame(data={'time':time_range_list, 'throughput':num_packet_list})
    if output_flag == True:
        dfi.to_csv(output_file,)
    dfi.plot(x ='time', y='throughput', kind = 'line')

    plt.xlabel('time')
    plt.ylabel('throughput (bytes/s)')

    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
