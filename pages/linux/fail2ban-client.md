# fail2ban-client

> Configure and control the fail2ban server.
> More information: <https://manned.org/fail2ban-client>.

- Show the general status of the fail2ban server and list active jails:

`fail2ban-client status`

- Show the status of a specific jail:

`fail2ban-client status {{jail}}`

- Remove a specific IP from a jail's ban list:

`fail2ban-client set {{jail}} unbanip {{ip_address}}`

- Verify that the fail2ban server is running:

`fail2ban-client ping`
