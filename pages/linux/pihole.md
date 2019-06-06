# pihole

> Terminal interface for the Pi-Hole ad-blocking DNS server.
> <https://pi-hole.net>.

- Check the Pi-hole daemon's status:

`pihole status`

- Monitor detailed system status:

`pihole chronometer`

- Start or stop the server:

`pihole {{enable|disable}}`

- Restart:

`pihole restartdns`

- Whitelist or blacklist a domain:

`pihole {{whitelist|blacklist}} {{reddit.com}}`

- Search the lists for a domain:

`pihole query {{reddit.com}}`
