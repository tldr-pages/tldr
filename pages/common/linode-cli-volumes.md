# linode-cli volumes

> Manage Linode Volumes.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/block-storage-volumes/>.

- List current Volumes:

`linode-cli volumes list`

- Create a new Volume and attach it to a specific Linode:

`linode-cli volumes create --label {{volume_label}} --size {{size_in_GB}} --linode-id {{linode_id}}`

- Attach a Volume to a specific Linode:

`linode-cli volumes attach {{volume_id}} --linode-id {{linode_id}}`

- Detach a Volume from a Linode:

`linode-cli volumes detach {{volume_id}}`

- Resize a Volume (Note: size can only be increased):

`linode-cli volumes resize {{volume_id}} --size {{new_size_in_GB}}`

- Delete a Volume:

`linode-cli volumes delete {{volume_id}}`
