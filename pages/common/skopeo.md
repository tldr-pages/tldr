# skopeo

> Container image management toolbox.
> Provides various utility commands to manage remote container images.
> More information: <https://github.com/containers/skopeo>.

- Inspect a remote image from a registry:

`skopeo inspect docker://{{registry.hostname}}/{{image:tag}}`

- List available tags for a remote image:

`skopeo list-tags docker://{{registry.hostname}}/{{image}}`

- Download an image from a registry:

`skopeo copy docker://{{registry.hostname}}/{{image:tag}} dir:{{path/to/directory/}}`

- Copy an image from one registry to another:

`skopeo copy docker://{source.registry}}/{{image:tag}} docker://{{destination.registry}}/{{image:tag}}`

- Delete an image from a registry:

`skopeo delete docker://{{registry.hostname}}/{{image:tag}}`

- Log in to a registry:

`skopeo login --username {{username}} {{registry.hostname}}`
