# linode-cli linodes

> Beheer Linode instanties.
> Bekijk ook: `linode-cli`.
> Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/linode-instances/>.

- Toon alle Linodes:

`linode-cli linodes list`

- Maak een nieuwe Linode:

`linode-cli linodes create --type {{linode_type}} --region {{region}} --image {{image_id}}`

- Bekijk details van een specifieke Linode:

`linode-cli linodes view {{linode_id}}`

- Werk de instellingen bij voor een Linode:

`linode-cli linodes update {{linode_id}} --label {{[new_label}}`

- Verwijder een Linode:

`linode-cli linodes delete {{linode_id}}`

- Voer een stroombeheer-operatie uit op een Linode:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- Toon alle beschikbare backups van een Linode:

`linode-cli linodes backups-list {{linode_id}}`

- Zet een backup terug naar een Linode:

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{backup_id}}`
