
# dns-sd

> Discover and resolve Bonjour (mDNS / DNS-SD) services.
> Common service types include `_http._tcp`, `_ipp._tcp`, `_airplay._tcp`.
> More info: <https://www.dns-sd.org/>.

- Browse for a service type on the local network (continuous until Ctrl-C):
  `dns-sd -B _http._tcp`

- Browse for a service type in a specific domain:
  `dns-sd -B _ftp._tcp dns-sd.org.`

- Resolve a specific service instance to host/port/TXT:
  `dns-sd -L "{{Instance Name}}" _ftp._tcp {{domain}}`

- Register (advertise) a local test service with TXT attributes:
  `dns-sd -R "{{My Service}}" _http._tcp local. {{8081}} {{path=/}} {{status=ok}}`

- List all service types currently advertised on the local link:
  `dns-sd -B _services._dns-sd._udp`

- Dump printer service records in DNS zone-file format:
  `dns-sd -Z _ipp._tcp`
