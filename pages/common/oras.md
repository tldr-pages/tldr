# oras

> OCI Registry As Storage - manage artifacts, images, and packages in OCI registries.
> More information: <https://oras.land/>.

- Push files to an OCI registry:

`oras push {{registry.example.com/repository:tag}} {{path/to/file1 path/to/file2 ...}}`

- Pull files from an OCI registry:

`oras pull {{registry.example.com/repository:tag}}`

- Copy an artifact between registries:

`oras cp {{source_registry/repo:tag}} {{destination_registry/repo:tag}}`

- Attach an artifact to an existing manifest reference:

`oras attach {{registry.example.com/repository:tag}} --artifact-type {{application/vnd.example.sbom}} {{path/to/file}}`

- Discover attachments and referrers for an artifact:

`oras discover {{registry.example.com/repository:tag}}`

- List tags in a remote repository:

`oras repo tags {{registry.example.com/repository}}`

- Log in to a remote registry:

`oras login {{registry.example.com}} --username {{username}}`

- Display help:

`oras --help`
