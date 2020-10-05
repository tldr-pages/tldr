# fail2ban-client

> Configure and control fail2ban server
> More information: <https://github.com/fail2ban/fail2ban/>

- Gets the current status of the jail service:

`fail2ban-client status {{jail}}`

- Manually unban IP from the jail service:

`fail2ban-client set {{jail}} unbanip {{ip}}`

- Verify fail2ban server is alive:

`fail2ban-client ping`
