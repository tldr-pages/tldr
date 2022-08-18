# gnmic get

> It is used to send a GetRequest to the specified target(s) (using the global flag --address and expects one GetResponse per target, per path.
> More information: <https://gnmic.kmrd.dev/cmd/get>.

- Get State of path:

`gnmic -a {{ip:port}} get --path {{path}}`

- Get RPC with multiple paths:

`gnmic -a {{ip:port}} get --path {{path1}} --path {{path2}}`

- Get RPC with path-prefix:

`gnmic -a {{ip:port}} get --prefix {{prefix}} --path {{path1}} --path {{path2}}`
