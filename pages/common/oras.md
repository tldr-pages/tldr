# oras

> Manage artifacts in OCI registries and image layouts.
> Some subcommands such as `pull`, `push`, and `manifest` have their own usage documentation.
> More information: <https://oras.land/docs/commands/use_oras_cli/>.

- Log in to a remote registry:

`oras login {{registry}}`

- Push a local file to a registry reference:

`oras push {{registry}}/{{repository}}:{{tag}} {{path/to/file}}`

- Pull artifact files from a registry reference:

`oras pull {{registry}}/{{repository}}:{{tag}}`

- Copy an artifact between registries:

`oras cp {{source_registry}}/{{repository}}:{{tag}} {{destination_registry}}/{{repository}}:{{tag}}`

- List repositories in a registry:

`oras repo ls {{registry}}`

- List tags for a repository:

`oras repo tags {{registry}}/{{repository}}`

- Tag an existing artifact with a new tag:

`oras tag {{registry}}/{{repository}}:{{tag}} {{new_tag}}`

- Show the installed ORAS version:

`oras version`
