# ufw limit

> Rate-limit connections through the firewall.
> Allows traffic by default, but denies further connection attempts if an IP address opens 6 or more connections within 30 seconds.
> More information: <https://manned.org/ufw>.

- Rate-limit traffic on a port (commonly used for SSH):

`sudo ufw limit {{22}}`

- Rate-limit traffic for a protocol on a port:

`sudo ufw limit {{22}}/{{tcp}}`

- Rate-limit a service by name:

`sudo ufw limit {{ssh}}`

- Rate-limit traffic from a specific source address:

`sudo ufw limit from {{source_address}}`

- Rate-limit a port with a comment for documentation:

`sudo ufw limit {{22}}/{{tcp}} comment '{{comment}}'`
