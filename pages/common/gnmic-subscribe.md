# gnmic subscribe

> Subscribe to a gnmic network device state updates.
> More information: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Subscribe to target state updates under the subtree of a specific path:

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}}`

- Subscribe to a target with a sample interval of 30s (default is 10s):

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}} --sample-interval 30s`

- Subscribe to a target with sample interval and updates only on change:

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}} --stream-mode on-change --heartbeat-interval {{1m}}`

- Subscribe to a target for only one update:

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}} --mode once`

- Subscribe to a target and specify response encoding (json_ietf):

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}} {{[-e|--encoding]}} json_ietf`
