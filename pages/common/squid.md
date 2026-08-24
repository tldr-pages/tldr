# squid

> Cache and forward HTTP requests through a proxy server.
> More information: <https://manned.org/squid>.

- Start Squid in the background:

`sudo squid`

- Start Squid in the foreground:

`sudo squid -N`

- Start Squid with a specific configuration file:

`sudo squid -f {{path/to/squid.conf}}`

- Test the configuration file for errors:

`sudo squid -k parse`

- Reload the configuration file:

`sudo squid -k reconfigure`

- Shut down Squid gracefully:

`sudo squid -k shutdown`

- Rotate the log files:

`sudo squid -k rotate`
