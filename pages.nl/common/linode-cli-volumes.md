# linode-cli volumes

> Beheer Linode Volumes.
> Bekijk ook: `linode-cli`.
> Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/block-storage-volumes/>.

- Toon alle huidige Volumes:

`linode-cli volumes list`

- Maak een nieuw Volume en koppel het aan een specifieke Linode:

`linode-cli volumes create --label {{volume_label}} --size {{size_in_GB}} --linode-id {{linode_id}}`

- Koppel een Volume aan een specifieke Linode:

`linode-cli volumes attach {{volume_id}} --linode-id {{linode_id}}`

- Koppel een Volume los van een Linode:

`linode-cli volumes detach {{volume_id}}`

- Vergroot een Volume (Let op: de grootte kan alleen toenemen):

`linode-cli volumes resize {{volume_id}} --size {{new_size_in_GB}}`

- Verwijder een Volume:

`linode-cli volumes delete {{volume_id}}`
