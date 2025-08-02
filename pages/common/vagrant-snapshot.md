# vagrant snapshot

> Manage snapshots of Vagrant machines.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/snapshot>.

- Take a snapshot of the machine (running or stopped):

`vagrant snapshot save {{snapshot_name}}`

- Restore a snapshot and start the machine:

`vagrant snapshot restore {{snapshot_name}}`

- Restore a snapshot without starting the machine:

`vagrant snapshot restore --no-start {{snapshot_name}}`

- Delete a snapshot:

`vagrant snapshot delete {{snapshot_name}}`

- List available snapshots of the machine:

`vagrant snapshot list`
