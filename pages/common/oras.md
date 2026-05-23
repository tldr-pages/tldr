# oras

> Manage artifacts, images, and packages in OCI registries and OCI image layouts.
> More information: <https://oras.land/docs/commands/use_oras_cli/>.

- Log in to a registry:

`oras login {{registry.example.com}}`

- Push a file to a registry:

`oras push {{registry.example.com/namespace/artifact:tag}} {{path/to/file}}`

- Pull files from a registry:

`oras pull {{registry.example.com/namespace/artifact:tag}}`

- List repositories under a registry:

`oras repo ls {{registry.example.com}}`

- List tags for a repository:

`oras repo tags {{registry.example.com/namespace/repository}}`

- Tag a manifest:

`oras tag {{registry.example.com/namespace/artifact:tag}} {{new_tag}}`

- Copy an artifact between registries:

`oras cp {{source_registry.example.com/namespace/artifact:tag}} {{destination_registry.example.com/namespace/artifact:tag}}`

- Attach a file to an existing artifact with a specific artifact type:

`oras attach --artifact-type {{application/vnd.example+type}} {{registry.example.com/namespace/artifact:tag}} {{path/to/file}}`
