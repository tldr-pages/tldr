# squid

> Cache and forward HTTP requests through a proxy server.
> More information: <https://manned.org/squid>.

- Start Squid in the background:

`squid`

- Start Squid in the foreground:

`squid -N`

- Start Squid with a specific configuration file:

`squid -f {{path/to/squid.conf}}`

- Test the configuration file for errors:

`squid -k parse`

- Reload the configuration file:

`squid -k reconfigure`

- Shut down Squid gracefully:

`squid -k shutdown`

- Rotate the log files:

`squid -k rotate`
