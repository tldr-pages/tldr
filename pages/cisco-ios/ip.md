# ip

> Manage IP configurations.
> Accessed in configuration mode.
> More information: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- Set the SSH version:

`ip ssh version {{2}}`

- Set the address of the device (This is done under `interface command`):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- Set the address to be determined with DHCP (This is done under `interface command`):

`ip address dhcp`

- Define a domain name:

`ip domain-name {{example.com}}`
