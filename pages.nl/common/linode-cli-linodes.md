# linode-cli linodes

> Beheer Linode instanties.
> Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- Toon alle Linodes:

`linode-cli linodes list`

- Maak een nieuwe Linode:

`linode-cli linodes create --type {{linode_type}} --region {{regio}} --image {{image_id}}`

- Bekijk details van een specifieke Linode:

`linode-cli linodes view {{linode_id}}`

- Werk de instellingen bij voor een Linode:

`linode-cli linodes update {{linode_id}} --label {{nieuw_label}}`

- Verwijder een Linode:

`linode-cli linodes delete {{linode_id}}`

- Voer een stroombeheeroperatie uit op een Linode:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- Toon alle beschikbare backups van een Linode:

`linode-cli linodes backups-list {{linode_id}}`

- Zet een backup terug naar een Linode:

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{backup_id}}`
