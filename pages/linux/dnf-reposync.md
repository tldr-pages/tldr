# dnf reposync

> Synchronize packages and metadata of a remote DNF repository to a local directory.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- Synchronize all packages from the repository with id “the_repo”. The synchronized copy is saved in “the_repo” subdirectory of the current working directory:

`dnf reposync --repoid={{the_repo}}`

- Synchronize all packages from the repository with id “the_repo”. In this case files are saved in “/path/to/directory” directory:

`dnf reposync -p {{/path/to/directory}} --repoid={{the_repo}}`

- Synchronize all packages and metadata from “the_repo” repository:

`dnf reposync --repoid={{the_repo}} --download-metadata`

- Download only newest packages per-repo:

`dnf reposync {{-n|--newest-only}} --repoid={{the_repo}}`

- Print just urls of what would be downloaded, don’t download:

`dnf reposync {{-u|--urls}} --repoid={{the_repo}}`

- Try to set the timestamps of the downloaded files to those on the remote side:

`dnf reposync --remote-time --repoid={{the_repo}}`
