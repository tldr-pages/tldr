# sniff.py

> Capture and display network packets using the `pcapy` library.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- List available network interfaces and select one to start capturing packets (requires `sudo`):

`sudo sniff.py`

- Capture packets and save output to a file while displaying it on the terminal:

`sudo sniff.py | sudo tee {{path/to/output_file}}`
