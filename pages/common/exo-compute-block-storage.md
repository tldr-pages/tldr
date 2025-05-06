# exo compute block-storage

> CLI for managing the Exoscale Block Storage service.
> More information: <https://community.exoscale.com/community/block-storage/>.

- Create a 20GB Block Storage Volume:

`exo compute block-storage create {{volume_name}} --size {{20}} {{[-z|--zone]}} {{zone}}`

- List Block Storage Volumes:

`exo compute block-storage list`

- Attach a Block Storage Volume to a Compute instance:

`exo compute block-storage attach {{volume_name|id}} {{instance_name|id}} {{[-z|--zone]}} {{zone}}`

- Forcefully detach a Block Storage Volume (does not require confirmation):

`exo compute block-storage detach {{volume_name|id}} {{[-z|--zone]}} {{zone}} {{[-f|--force]}}`

- Create a snapshot of a Block Storage Volume:

`exo compute block-storage snapshot create {{volume_name|id}} --name {{snapshot_name}} {{[-z|--zone]}} {{zone}}`

- Create a Block Storage Volume from a snapshot:

`exo compute block-storage create {{volume_name}} --snapshot {{snapshot_name|id}} {{[-z|--zone]}} {{zone}}`

- Update an existing Block Storage Volume:

`exo compute block-storage update {{volume_name|id}} --size {{new_size}} --name {{new_name}}`
