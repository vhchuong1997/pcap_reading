# pcap_reading

Converting wireshark packet capture (pcap) into info, illustrations, etc.

## Requirements
- wireshark
- python 3.6
- [mscgen](https://www.mcternan.me.uk/mscgen/) (optional, for convering to image files)

## Installation
`git clone https://github.com/vhchuong1997/pcap_reading.git`

## Usage
- `python pcaptotxt.py -i <pcap_file_input> -o <txt_file_output>`

	The method will read the input pcap file and write the specified parameters from the pcap file to txt file.
	Example: `python pcaptotxt.py -i 'broadcom.pcap' -o 'result.txt'`

- `python visualize_throughput.py -i <pcap_file_input>`
	The method will read the input pcap file and draw throughput figure (line format)
	Example: `python visualize_throughput.py -i 'broadcom.pcap'

## Hackmd Page
### [hackmd page](https://hackmd.io/@Jon97/HyzTUOY2u)

## License
This project is licensed under MIT. Contributions to this project are accepted under the same license.
