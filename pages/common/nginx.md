# nginx

> nginx web server

- Start server with default config

`nginx`

- Start server with custom config file

`nginx -c {{config_file}}`

- Start server with a prefix for all relative paths in config file

`nginx -c {{config_file}} -p {{prefix/for/relative/paths}}`

- Test configuration without affecting the running server

`nginx -t`
