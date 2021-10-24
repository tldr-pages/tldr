# tlmgr

> Manages packages and configuration options of an existing TeX Live installation.
> Some subcommands such as `tlmgr paper` have their own usage documentation.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Install a package and its dependencies:

`tlmgr install {{package}}`

- Remove a package and its dependencies:

`tlmgr remove {{package}}`

- Display information about a package:

`tlmgr info {{package}}`

- Update all packages:

`tlmgr update --all`

- Show possible updates without updating anything:

`tlmgr update --list`

- Start a GUI version of tlmgr:

`tlmgr gui`

- List all TeX Live configurations:

`tlmgr conf`
