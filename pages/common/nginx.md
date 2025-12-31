# nginx

> Nginx web server.
> More information: <https://nginx.org/docs/switches.html>.

- Start the server with the default configuration file:

`nginx`

- Start the server with a custom configuration file:

`nginx -c {{configuration_file}}`

- Start the server with a prefix for all relative paths in the configuration file:

`nginx -c {{configuration_file}} -p {{path/to/prefix}}`

- Test the configuration without affecting the running server:

`nginx -t`

- Reload the configuration by sending a signal with no downtime:

`nginx -s reload`
