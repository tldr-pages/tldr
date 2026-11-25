# proxychains

> Run a program with its TCP connections routed through configured proxy servers.
> More information: <https://github.com/rofl0r/proxychains-ng>.

- Run a program through the proxies in the default configuration:

`proxychains {{program}}`

- Run a program using a specific configuration file:

`proxychains -f {{path/to/proxychains.conf}} {{program}}`

- Run a program without printing proxychains status messages:

`proxychains -q {{program}}`

- Run a program quietly using a specific configuration file:

`proxychains -q -f {{path/to/proxychains.conf}} {{program}}`
