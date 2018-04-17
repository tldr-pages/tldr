# apache2ctl

> The CLI tool to administrate HTTP web server Apache.
> This commmand comes with Debian based OS, for RHEL based OS see httpd.

- Start the Apache daemon.  Give an error if it is already running:

`apache2ctl start`

- Stop the Apache daemon:

`apache2ctl stop`

- Restart the Apache daemon:

`apache2ctl restart`

- Check configuration syntax file:

`apache2ctl -t`

- Print loaded modules list:

`apache2ctl -M`
