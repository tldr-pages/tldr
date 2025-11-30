# dnsmasq

> Lightweight DNS, DHCP, TFTP, and PXE server.
> More information: <https://manned.org/dnsmasq>.

- Start dnsmasq with default configuration:

`dnsmasq`

- Run dnsmasq in the foreground (for debugging):

`dnsmasq --no-daemon`

- Specify a custom configuration file:

`dnsmasq --conf-file={{path/to/config.conf}}`

- Enable verbose logging:

`dnsmasq --log-queries --log-facility=-`

- Set a DHCP range and lease time:

`dnsmasq --dhcp-range={{192.168.0.50,192.168.0.150,12h}}`

- Display version:

`dnsmasq --version`
