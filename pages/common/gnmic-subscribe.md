# gnmic subscribe

> It is used to send a Subscribe Request to the specified target(s) and expects one or multiple Subscribe Response
> More information: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Subscribe to a target:

`gnmic -a {{ip:port}} subscribe --path {{path}}`

- Subscribe to a target with a sample interval of 30s (default is 10s):

`gnmic -a {{ip:port}} sub --path {{path}} --sample-interval 30s`

- Subscribe to a target with sample interval and updates only on change:

`gnmic -a {{ip:port}} subscribe --path {{path}} --stream-mode on-change --heartbeat-interval 1m`

- Subscribe to a target once:

`gnmic -a {{ip:port}} subscribe --path {{path}} --mode once`
