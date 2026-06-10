# դնսմասք

> Թեթև DNS, DHCP, TFTP և PXE սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/dnsmasq>:.

- Սկսեք dnsmasq-ը լռելյայն կազմաձևով.:

`dnsmasq`

- Գործարկել dnsmasq-ը առաջին պլանում (վրիպազերծման համար).:

`dnsmasq --no-daemon`

- Նշեք հատուկ կազմաձևման ֆայլ.:

`dnsmasq --conf-file={{path/to/config.conf}}`

- Միացնել մանրամասն գրանցումը.:

`dnsmasq --log-queries --log-facility=-`

- Սահմանեք DHCP միջակայք և վարձակալության ժամանակը.:

`dnsmasq --dhcp-range={{192.168.0.50,192.168.0.150,12h}}`

- Ցուցադրման տարբերակը:

`dnsmasq --version`
