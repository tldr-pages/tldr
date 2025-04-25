# fail2ban-client

> Configure and control fail2ban server.
> More information: <https://manned.org/fail2ban-client>.

- Retrieve current status of the jail service:

`fail2ban-client status {{jail}}`

- Remove the specified IP from the jail service's ban list:

`fail2ban-client set {{jail}} unbanip {{ip}}`

- Verify fail2ban server is alive:

`fail2ban-client ping`
