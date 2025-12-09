# pihole

> Manage the Pi-hole ad-blocking DNS server.
> More information: <https://docs.pi-hole.net/main/pihole-command>.

- Check Pi-hole's status:

`pihole status`

- Update Pi-hole and Gravity:

`sudo pihole {{[-up|updatePihole]}}`

- Start or stop the daemon:

`pihole {{enable|disable}}`

- Update the lists and flush the cache without restarting the DNS server:

`pihole reloaddns`

- Update the list of ad-serving domains:

`pihole {{[-g|updateGravity]}}`

- Allow or deny the specified domain:

`pihole {{allow|deny}} {{example.com}}`

- Search the lists for a domain:

`pihole {{[-q|query]}} {{example.com}}`

- Open a real-time log of connections:

`pihole {{[-t|tail]}}`
