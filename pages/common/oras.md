# oras

> Manage artifacts in OCI registries and image layouts.
> More information: <https://oras.land/docs/commands/use_oras_cli>.

- List available subcommands:

`oras help`

- Show the installed ORAS version:

`oras version`

- Log in to a remote registry interactively:

`oras login {{registry}}`

- Push a file to a registry reference:

`oras push {{registry}}/{{repository}}:{{tag}} {{path/to/file}}`

- Pull artifact files from a registry reference:

`oras pull {{registry}}/{{repository}}:{{tag}}`

- Copy an artifact between registries:

`oras cp {{source_registry}}/{{repository}}:{{tag}} {{destination_registry}}/{{repository}}:{{tag}}`
