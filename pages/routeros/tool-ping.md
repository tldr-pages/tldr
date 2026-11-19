# tool ping

> Send ICMP ECHO_REQUEST packets to network hosts.
> More information: <https://manual.mikrotik.com/docs/cli-reference/tool/ping>.

- Ping a host with IP `10.0.0.1` (Note: `10.0.0.1` can be shortened to `10.1`):

`/tool/ping 10.0.0.1`

- Ping a host only a specific number of times:

`/tool/ping count={{count}} {{host}}`

- Ping host, specifying the interval in seconds between requests (default is 1 second):

`/tool/ping interval={{seconds}} {{host}}`

- Ping host from a specific interface and on behalf of a specific router's IP address assigned to the interface:

`/tool/ping interface={{ether1}} src-address={{router_ip}} {{host}}`

- Ping all IPv6 local network hosts:

`/tool/ping ff02::1%{{ether1}}`
