# apachectl

> Control an Apache HTTP server.
> More information: <https://manned.org/apachectl>.

- Start the server:

`sudo apachectl start`

- Restart the server:

`sudo apachectl restart`

- Stop the server:

`sudo apachectl stop`

- Test configuration file validity:

`apachectl configtest`

- Check server status (requires the lynx browser):

`apachectl status`

- Reload configuration without dropping connections:

`sudo apachectl graceful`

- Print full Apache configuration:

`apachectl -S`

- Display help:

`apachectl -h`
