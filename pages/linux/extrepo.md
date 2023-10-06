# extrepo

> Manage external Debian repositories.
> The extrepo tool is used to manage external repositories in Debian.
> More information: <https://manpages.ubuntu.com/manpages/focal/man1/extrepo.1p.html>.

- Search for a given package:

`extrepo search {{key}}`

- Enable the repository named {{repository_name}}: 

`sudo extrepo enable {{repository_name}}`

- Disable the repository named {{repository_name}}: 

`sudo extrepo disable {{repository_name}}`

- Update the repository named {{repository_name}}: 

`sudo extrepo update {{repository_name}}`
