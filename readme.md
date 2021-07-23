# pcaptomsc

converting wireshark packet capture (pcap) into message sequence chart for sequencediagram.net, hackmd.io, or mscgen (png, svg, and eps format).

## Requirements
- wireshark
- python 3.3
- [mscgen](https://www.mcternan.me.uk/mscgen/) (optional, for convering to image files)

## Installation
`git clone https://github.com/Jonathan2106/pcaptomsc.git pcaptomsc`

## Usage
- `python pcaptomsc.py -f <format> -i <pcap_file_input> -o <text_file_output>`

	the method above will result specified format msc displayed in terminal and saved in the text_file_output

	supported output text format:
	- sequencediagram (sequencediagram.net)
	- hackmd (hackmd.io)
	- mscgen

- `python pcaptomsc.py -i <pcap_file_input>`

	the method above will result hackmd formatted msc displayed in terminal

- `python pcaptomsc.py -f mscgen -i <pcap_file_input> -o <image_file_output>`

	the method above will result specified format msc displayed in terminal, msc file output, and image file.

	supoported image format (based on mscgen):
	- png
	- eps
	- svg

- `python pcaptomsc.py -f mscgen -i <pcap_file_input> -o <text_file_output> -o <image_file_output>`

	the method above will result specified format msc displayed in terminal, text file output, msc file output, and image file.
	
## Examples

example captures are obtained from [SampleCapture](https://wiki.wireshark.org/SampleCaptures)

### DHCP
- `python pcaptomsc.py -f mscgen -i ./example/dhcp.pcap -o ./example/dhcp.png`
![](https://i.imgur.com/7lVwnF7.png)

- `python pcaptomsc.py -f hackmd -i ./example/smtp.pcap -o ./example/smtp.txt `
```
0.0.0.0 -> 255.255.255.255: *DHCP*: DHCP Discover - Transaction ID 0x3d1d
192.168.0.1 -> 192.168.0.10: *DHCP*: DHCP Offer - Transaction ID 0x3d1d
0.0.0.0 -> 255.255.255.255: *DHCP*: DHCP Request - Transaction ID 0x3d1e
192.168.0.1 -> 192.168.0.10: *DHCP*: DHCP ACK - Transaction ID 0x3d1e
```

### OSPF
- `python pcaptomsc.py -f mscgen -i ./example/ospf.cap -o ./example/ospf.png`
![](https://i.imgur.com/2T7cRFD.png)


- `python pcaptomsc.py -f hackmd -i ./example/ospf.cap -o ./example/ospf.txt `
```
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.2 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.2 -> 224.0.0.5: *OSPF*: Hello Packet
192.168.170.8 -> 192.168.170.2: *OSPF*: DB Description
192.168.170.2 -> 192.168.170.8: *OSPF*: DB Description
192.168.170.2 -> 192.168.170.8: *OSPF*: DB Description
192.168.170.8 -> 192.168.170.2: *OSPF*: DB Description
192.168.170.2 -> 192.168.170.8: *OSPF*: DB Description
192.168.170.8 -> 192.168.170.2: *OSPF*: DB Description
192.168.170.2 -> 192.168.170.8: *OSPF*: DB Description
192.168.170.2 -> 192.168.170.8: *OSPF*: LS Request
192.168.170.8 -> 192.168.170.2: *OSPF*: LS Request
192.168.170.8 -> 224.0.0.5: *OSPF*: LS Update
192.168.170.2 -> 224.0.0.6: *OSPF*: LS Update
192.168.170.2 -> 224.0.0.6: *OSPF*: LS Update
192.168.170.8 -> 224.0.0.5: *OSPF*: LS Update
192.168.170.8 -> 224.0.0.5: *OSPF*: LS Update
192.168.170.8 -> 224.0.0.5: *OSPF*: LS Acknowledge
192.168.170.2 -> 224.0.0.6: *OSPF*: LS Update
192.168.170.8 -> 224.0.0.5: *OSPF*: LS Acknowledge
192.168.170.2 -> 192.168.170.8: *OSPF*: LS Update
192.168.170.8 -> 192.168.170.2: *OSPF*: LS Acknowledge
192.168.170.2 -> 224.0.0.6: *OSPF*: LS Update
192.168.170.8 -> 192.168.170.2: *OSPF*: LS Acknowledge
192.168.170.8 -> 224.0.0.5: *OSPF*: Hello Packet
```

## Hackmd Page
[hackmd page](https://hackmd.io/@Jon97/HyzTUOY2u)

## License
This project is licensed under MIT. Contributions to this project are accepted under the same license.
