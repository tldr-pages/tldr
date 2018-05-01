# apache2ctl

> The CLI tool to administrate HTTP web server Apache.
> This commmand comes with Debian based OS, for RHEL based OS see httpd.

- Start the Apache daemon. Throw an error if it is already running:

`sudo apache2ctl start`

- Stop the Apache daemon:

`sudo apache2ctl stop`

- Restart the Apache daemon:

`sudo apache2ctl restart`

- Test syntax of the configuration file:

`sudo apache2ctl -t`

- List loaded modules:

`sudo apache2ctl -M`
