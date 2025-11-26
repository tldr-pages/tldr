# squid

> A high-performance caching and forwarding HTTP web proxy.
> More information: <https://manned.org/squid>.

- Start the Squid daemon:

`squid`

- Start Squid daemon with a specific configuration file:

`squid -f {{path/to/squid.conf}}`

- Parse and test the configuration file for errors:

`squid -k parse`

- Reconfigure Squid (reload configuration file without stopping):

`squid -k reconfigure`

- Gracefully shutdown Squid:

`squid -k shutdown`

- Immediately shutdown Squid:

`squid -k kill`

- Rotate log files:

`squid -k rotate`

- Check the status of the running Squid process:

`squid -k check`
