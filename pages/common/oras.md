# oras

> OCI Registry As Storage - manage OCI artifacts, images, and packages.
> More information: <https://oras.land/docs/commands/use_oras_cli/>.

- Log in to a remote OCI registry:

`oras login --username {{username}} --password {{password}} {{registry.example.com}}`

- Push files to a registry with a specific tag:

`oras push {{registry.example.com/namespace/repo:tag}} {{path/to/file1 path/to/file2 ...}}`

- Pull files from a registry:

`oras pull {{registry.example.com/namespace/repo:tag}}`

- Copy an artifact between registries:

`oras copy {{registry1.example.com/namespace/repo:tag}} {{registry2.example.com/namespace/repo:tag}}`

- Tag an existing artifact in a registry:

`oras tag {{registry.example.com/namespace/repo:tag}} {{new_tag}}`

- List repositories in a registry:

`oras repo list {{registry.example.com}}`

- List tags for a repository in a registry:

`oras repo tags {{registry.example.com/namespace/repo}}`

- Fetch and display the manifest of an artifact:

`oras manifest fetch {{registry.example.com/namespace/repo:tag}}`
