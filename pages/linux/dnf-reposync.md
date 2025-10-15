# dnf reposync

> Synchronize packages and metadata of a remote DNF repository to a local directory.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- Synchronize all packages from the repository with id `repo_name`. The synchronized copy is saved in `repo_name` subdirectory of the current working directory:

`dnf reposync --repoid {{repo_name}}`

- Synchronize all packages and define a custom save location:

`dnf reposync {{[-p|--download-path]}} {{path/to/directory}} --repoid {{repo_name}}`

- Synchronize all packages and metadata:

`dnf reposync --repoid {{repo_name}} --download-metadata`

- Download only newest packages per-repo:

`dnf reposync {{[-n|--newest-only]}} --repoid {{repo_name}}`

- Print just urls of what would be downloaded, don’t download:

`dnf reposync {{[-u|--urls]}} --repoid {{repo_name}}`

- Try to set the timestamps of the downloaded files to those on the remote side:

`dnf reposync --remote-time --repoid {{repo_name}}`
