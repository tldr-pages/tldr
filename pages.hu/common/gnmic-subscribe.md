# gnmic subscribe

> Feliratkozás egy gnmic hálózati eszköz állapotfrissítésére. További információ: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Feliratkozás egy adott útvonal alfája alatti célállapot-frissítésekre:

`gnmic --address {{ip:port}} subscribe --path {{path}}`

- Feliratkozás egy célpontra 30 másodperces mintavételi időközzel (alapértelmezett 10 másodperc):

`gnmic -a {{ip:port}} subscribe --path {{path}} --sample-interval 30s`

- Feliratkozás egy célpontra mintaintervallummal és csak változáskor történő frissítéssel:

`gnmic -a {{ip:port}} subscribe --path {{path}} --stream-mode on-change --heartbeat-interval 1m`

- Feliratkozás egy célpontra csak egy frissítésre:

`gnmic -a {{ip:port}} subscribe --path {{path}} --mode once`

- Feliratkozás egy célpontra és válaszkódolás megadása (json_ietf):

`gnmic -a {{ip:port}} subscribe --path {{path}} --encoding json_ietf`
