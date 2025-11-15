# knock

> Port knocking client to open specific ports on firewall.
> More information: <https://manned.org/knock>.

- Knock on ports using different protocols:

`knock {{hostname}} {{portnumber}}:{{protocol}}`

- Knock on port using UDP:

`knock {{[-u|--udp]}} {{hostname}} {{portnumber}}`

- Force usage of IPv4/IPv6:

`knock {{-4|-6}} {{hostname}} {{portnumber}}`

- Display errors and details of connection:

`knock {{[-v|--verbose]}} {{hostname}} {{portnumber}}`
