# dnf reposync

> Synchronize packages and metadata of a remote DNF repository to a local directory.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- Synchronize all packages from the repository with id `repo_name` to a subdirectory `repo_name` of the current working directory:

`dnf reposync --repoid {{repo_name}}`

- Synchronize all packages and define a custom save location:

`dnf reposync --repoid {{repo_name}} {{[-p|--download-path]}} {{path/to/directory}}`

- Synchronize all packages and metadata:

`dnf reposync --repoid {{repo_name}} --download-metadata`

- Download only newest packages per-repo:

`dnf reposync --repoid {{repo_name}} {{[-n|--newest-only]}}`

- Just print URLs of what would be downloaded, don’t download:

`dnf reposync --repoid {{repo_name}} {{[-u|--urls]}}`

- Try to set the timestamps of the downloaded files to those on the remote side:

`dnf reposync --repoid {{repo_name}} --remote-time`
