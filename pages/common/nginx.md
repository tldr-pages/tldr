# nginx

> Nginx web server.
> More information: <https://nginx.org/en/>.

- Start server with the default configuration file:

`nginx`

- Start server with a custom configuration file:

`nginx -c {{configuration_file}}`

- Start server with a prefix for all relative paths in the configuration file:

`nginx -c {{configuration_file}} -p {{prefix/for/relative/paths}}`

- Test the configuration without affecting the running server:

`nginx -t`

- Reload the configuration by sending a signal with no downtime:

`nginx -s reload`
