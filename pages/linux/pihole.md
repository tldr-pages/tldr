# pihole

> Terminal interface for the Pi-Hole ad-blocking DNS server.
> More information: <https://pi-hole.net>.

- Check status:

`pihole status`

- Monitor detailed status:

`pihole chronometer`

- Start or stop the server:

`pihole {{enable|disable}}`

- Restart:

`pihole restartdns`

- Whitelist or blacklist a domain:

`pihole {{whitelist|blacklist}} {{reddit.com}}`

- Search the lists for a domain:

`pihole query {{reddit.com}}`
