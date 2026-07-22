# dns-sd

> Discover, resolve, and advertise network services using Multicast DNS (mDNS) and DNS Service Discovery (DNS-SD).
> More information: <https://keith.github.io/xcode-man-pages/dns-sd.1.html>.

- Browse for all HTTP services in the local domain:

`dns-sd -B {{_http._tcp}} local`

- Resolve a service and display its hostname, port, and TXT records:

`dns-sd -L "{{service_name}}" {{_http._tcp}} local`

- Look up IPv4 and IPv6 addresses for a hostname:

`dns-sd -G v4v6 {{hostname}}`

- Query a DNS resource record:

`dns-sd -q {{hostname}} {{A}} {{IN}}`

- Advertise an HTTP service on a specific port:

`dns-sd -R "{{service_name}}" {{_http._tcp}} local {{port}}`

- Display the version of the running mDNSResponder daemon:

`dns-sd -V`
