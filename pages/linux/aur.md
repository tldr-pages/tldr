# aur

> Build packages from AUR and manage local repositories.
> More information: <https://github.com/aurutils/aurutils>.

- Search the AUR database for a keyword:

`aur search {{package}}`

- Download a package and its dependencies from AUR, build them and add them to a local repository:

`aur sync {{package}}`

- List packages that are available in your local repository:

`aur repo -l`

- Upgrade local repository packages:

`aur sync -u`
