# apache2ctl

> apache2ctl (alternatively apachectl)is a front end to the Apache HyperText Transfer Protocol (HTTP) server.  It is designed to help the administrator control the functioning of the Apache apache2 daemon.
> This commmand comes with Debian based Apache package.

- Start the Apache daemon.  Gives an error if it is already running:

`apache2ctl start`

- Stops the Apache daemon.

`apache2ctl stop`

- Restart the Apache daemon.

`apache2ctl restart`

- Check Apache configuration syntax file.

`apache2ctl -t`

- Print loaded Apache Modules:

`apache2ctl -M`
