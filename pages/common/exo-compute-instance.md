# exo compute instance

> Manage Exoscale Compute instances.
> More information: <https://community.exoscale.com/product/compute/instances/>.

- Create a Debian based Compute instance with a disk size of 10GB:

`exo compute instance create --disk-size 10 {{instance_name}} {{[-z|--zone]}} {{zone}} --template '{{Linux Debian 12 (Bookworm) 64-bit}}'`

- Log into a Compute instance via SSH:

`exo compute instance ssh {{instance_name|id}}`

- List all of the Compute instances:

`exo compute instance list`

- Add an instance to a Security Group:

`exo compute instance security-group add {{instance_name|id}} {{security_group_name|id}}`

- Scale the size of a Compute instance:

`exo compute instance scale {{instance_name|id}} {{instance_type}}`

- Create a snapshot of a Compute instance:

`exo compute instance snapshot create {{instance_name|id}}`

- Revert a Compute instance to a snapshot (the data written after the snapshot has been created will be lost):

`exo compute instance snapshot revert {{snapshot_id}} {{instance_name|id}}`

- Resize the disk size of a Compute instance to 20GB:

`exo compute instance resize-disk {{instance_name|id}} 20`
