# gnmic

> A gNMI CLI client that provides full support for Capabilities, Get, Set and Subscribe RPCs with collector capabilities.
> More information: <https://gnmic.kmrd.dev>.

- Request capabilities (gnmic capabilities):

`gnmic --address {{ip:port}} --insecure capabilities`

- Username and password can be given to any command:

`gnmic --address {{ip:port}} --username {{username}} --password {{password}} --insecure capabilities`

- Get request (gnmic get):

`gnmic -a {{ip:port}} --insecure get --path {{path}}`

- Set request (gnmic set):

`gnmic -a {{ip:port}} --insecure set --update-path {{path}} --update-value {{value}}`

- Subscribe request (gnmic subscribe):

`gnmic -a {{ip:port}} --insecure subscribe --path {{path}}`
