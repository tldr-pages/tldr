# squid

> Caching and forwarding HTTP web proxy server.
> Commonly used for access control, caching, and traffic monitoring.
> More information: <https://www.squid-cache.org>.

- Start Squid with the default configuration:

`sudo squid`

- Check configuration syntax for errors:

`sudo squid -k parse`

- Reload configuration without restarting:

`sudo squid -k reconfigure`

- Stop the Squid service:

`sudo squid -k shutdown`

- Clear cache (stop Squid first):

`sudo squid -k shutdown && sudo rm -rf /var/spool/squid/* && sudo squid`
