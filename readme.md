# pcap_reading

Converting wireshark packet capture (pcap) into info, illustrations, etc.

## Requirements
- wireshark
- python 3.6
- [mscgen](https://www.mcternan.me.uk/mscgen/) (optional, for convering to image files)

## Installation
`git clone https://github.com/vhchuong1997/pcap_reading.git`

## Usage
- `python pcaptolist.py -i <pcap_file_input> -o <txt_file_output>`

	The method will read th inpute pcap file and write the specified parameters from the pcap file to txt file.
	Example: `python pcaptolist.py -i 'broadcom.pcap' -o 'result.txt'`

## Hackmd Page
### [hackmd page](https://hackmd.io/@Jon97/HyzTUOY2u)

## License
This project is licensed under MIT. Contributions to this project are accepted under the same license.
