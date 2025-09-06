# ctr

> Manage `containerd` containers and images.
> More information: <https://containerd.io>.

- List all containers (running and stopped):

`ctr containers list`

- List all images:

`ctr images list`

- Pull an image:

`ctr images pull {{image}}`

- Tag an image:

`ctr images tag {{source_image}}:{{source_tag}} {{target_image}}:{{target_tag}}`
