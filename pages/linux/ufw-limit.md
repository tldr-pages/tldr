# ufw limit

> Rate limit connections to deny an IP initiating 6 or more attempts within 30 seconds.
> More information: <https://manned.org/ufw>.

- Simulate a rule without applying it:

`sudo ufw --dry-run limit {{profile}}`

- Rate limit a specific service by profile:

`sudo ufw limit {{profile}}`

- Rate limit a specific port and protocol:

`sudo ufw limit {{22}}/{{tcp}}`

- Rate limit only from a specific source address or subnet:

`sudo ufw limit from {{192.168.0.0/16}} to any port {{22}} proto {{tcp}}`

- Rate limit on a specific network interface:

`sudo ufw limit in on {{eth0}} to any port {{22}}`

- Delete a limit rule:

`sudo ufw delete limit {{service|port}}/{{tcp}}`
