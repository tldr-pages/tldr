# emaint-sync

> Synchronize Portage repositories.
> More info: <https://wiki.gentoo.org/wiki/Portage#emaint>.

- Synchronize repositories that are set to auto-sync (default for most repositories):

`sudo emaint sync --auto`

- Synchronize a specific repository:

`sudo emaint sync --repo {{repository}}`

- Synchronize all repositories:

`sudo emaint sync --allrepos`
