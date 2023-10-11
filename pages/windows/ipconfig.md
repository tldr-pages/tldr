# ipconfig

> Display and manage the network configuration of Windows.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Show a list of network adapters:

`ipconfig`

- Show a detailed list of network adapters:

`ipconfig /all`

- Renew the IP addresses for a network adapter:

`ipconfig /renew {{adapter}}`

- Free up the IP addresses for a network adapter:

`ipconfig /release {{adapter}}`

- Show the local DNS cache:

`ipconfig /displaydns`

- Remove all data from the local DNS cache:

`ipconfig /flushdns`
