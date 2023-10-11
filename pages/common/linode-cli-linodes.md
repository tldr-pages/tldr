# linode-cli linodes

> Manage Linode instances.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/linode-instances/>.

- List all Linodes:

`linode-cli linodes list`

- Create a new Linode:

`linode-cli linodes create --type {{linode_type}} --region {{region}} --image {{image_id}}`

- View details of a specific Linode:

`linode-cli linodes view {{linode_id}}`

- Update settings for a Linode:

`linode-cli linodes update {{linode_id}} --label {{[new_label}}`

- Delete a Linode:

`linode-cli linodes delete {{linode_id}}`

- Perform a power management operation on a Linode:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- List available backups for a Linode:

`linode-cli linodes backups-list {{linode_id}}`

- Restore a backup to a Linode:

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{backup_id}}`
