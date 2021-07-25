import pyshark
import pandas as pd
import matplotlib.pyplot as plt


capture = pyshark.FileCapture('broadcom.pcap')

# last_packet = capture[-1:]
# last_time = round(last_packet.frame_info.time_relative)

time_list = []
frlen_list = []
sum_len = 0
for packet in capture:
    time_list.append(float(packet.frame_info.time_relative))
    frlen_list.append(float(packet.length))

d = {'time':time_list,'frame length':frlen_list}
df = pd.DataFrame(data=d)
# last_packet = capture[-1:]
# last_time = round(last_packet.frame_info.time_relative)
final_time = round(df.iloc[-1:]['time'].values[0])
print(final_time)

time_range_list = []
num_packet_list = []

for i in range(1,final_time+1):
    dfi = df.loc[(df['time'] <= i) & (df['time'] >= i-1)]
    time_range_list.append(i-1)
    num_packet_list.append(dfi['frame length'].sum())
    del(dfi)

dfi = pd.DataFrame(data={'time':time_range_list, 'throughput':num_packet_list})
dfi.plot(x ='time', y='throughput', kind = 'line')
# dfi.plot(x ='time', y='throughput', drawstyle = 'steps')
plt.xlabel('time')
plt.ylabel('throughput (bytes/s)')

plt.show()