# wol

> Client for sending Wake-on-LAN magic packets.
> More information: <https://sourceforge.net/projects/wake-on-lan/>.

- Send a WoL packet to a device:

`wol {{mac_adress}}`

- Send a WoL packet to a device in another subnet based on its IP:

`wol --ipaddr={{ip_address}} {{mac_adress}}`

- Send a WoL packet to a device in another subnet based on its hostname:

`wol --host={{hostname}} {{mac_adress}}`

- Send a WoL packet to a specific port:

`wol --port={{porn_number}}`

- Read hardware addresses, IP addresses/hostnames, optional ports and SecureON password from a file:

`wol --file={{path/to/file}}`

- Turn on verbose input:

`wol --verbose {{mac_adress}}`
