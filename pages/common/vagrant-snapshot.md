# vagrant snapshot

> Manage snapshots of Vangrant machines:
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/snapshot>.

- Take a snapshot of the machine (running or stopped):

`vagrant snpahot save {{snapshot_name}}`

- Restore a snapshot and start the machine:

`vagrant snapshot restore {{snapshot_name}}`

- Restore a snapshot but do not start the machine:

`vagrant snapshot restore --no-start {{snapshot_name}}`

- Delete a snapshot:

`vagrant snspahot delete {{snapshot_name}}`

- List available snapshots of the machine:

`vagrant snapshot list`
