# gnmic subscribe

> Abonneer op gnmic netwerk apparaat status updates.
> Meer informatie: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Abonneer op doel status updates onder de subtree van een specifiek pad:

`gnmic --address {{ip:poort}} subscribe --path {{pad}}`

- Abonneer op een doel met een interval van 30 seconden (standaard is 10 seconden):

`gnmic -a {{ip:poort}} subscribe --path {{pad}} --sample-interval 30s`

- Abonneer op een doel met een interval en alleen op updates bij verandering:

`gnmic -a {{ip:poort}} subscribe --path {{pad}} --stream-mode on-change --heartbeat-interval 1m`

- Abonneer op een doel voor alleen een update:

`gnmic -a {{ip:poort}} subscribe --path {{pad}} --mode once`

- Abonneer op een doel en specificeer de response codering (json_ietf):

`gnmic -a {{ip:poort}} subscribe --path {{pad}} --encoding json_ietf`
