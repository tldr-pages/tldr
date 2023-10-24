# dhcpig

> Initiates an advanced DHCP exhaustion attack and stress test.
> DHCPig needs to be run with root privileges.
> More information: <https://github.com/kamorin/DHCPig>.

- Exhaust all of the available DHCP addresses using the specified interface:

`sudo ./pig.py {{eth0}}`

- Exhaust IPv6 addresses using eth1 interface:

`sudo ./pig.py -6 {{eth1}}`

- Send fuzzed/malformed data packets using the interface:

`sudo ./pig.py --fuzz {{eth1}}`

- Enable color output:

`sudo ./pig.py -c {{eth1}}`

- Enable minimal verbosity and color output:

`sudo ./pig.py -c --verbosity=1 {{eth1}}`

- Set debug verbosity and scan network of neighboring devices using ARP packets:

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp {{eth1}}`

- Enable printing lease information, attempt to scan and release all neighbor IP addresses:

`sudo ./pig.py --neighbors-scan-arp -r --show-options {{eth1}}`
