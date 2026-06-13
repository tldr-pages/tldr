# dhcpig

> Initiates an advanced DHCP exhaustion attack and stress test.
> More information: <https://github.com/kamorin/DHCPig#usage>.

- Exhaust all of the available DHCP addresses using the specified interface:

`sudo {{path/to}}/pig.py {{eth0}}`

- Exhaust IPv6 addresses using eth1 interface:

`sudo {{path/to}}/pig.py {{[-6|--ipv6]}} {{eth1}}`

- Send fuzzed/malformed data packets using the interface:

`sudo {{path/to}}/pig.py {{[-f|--fuzz]}} {{eth1}}`

- Enable color output:

`sudo {{path/to}}/pig.py {{[-c|--color]}} {{eth1}}`

- Enable minimal verbosity and color output:

`sudo {{path/to}}/pig.py {{[-c|--color]}} {{[-v|--verbosity]}} 1 {{eth1}}`

- Use a debug verbosity of 100 and scan network of neighboring devices using ARP packets:

`sudo {{path/to}}/pig.py {{[-c|--color]}} {{[-v|--verbosity]}} 100 {{[-n|--neighbors-scan-arp]}} {{eth1}}`

- Enable printing lease information, attempt to scan and release all neighbor IP addresses:

`sudo {{path/to}}/pig.py {{[-n|--neighbors-scan-arp]}} {{[-r|--neighbors-attack-release]}} {{[-o|--show-options]}} {{eth1}}`
