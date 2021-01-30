# gdebi

> Simple tool to install deb files.
> More information: <https://launchpad.net/gdebi>.

- Install local deb packages resolving and installing its dependencies:

`gdebi {{path/to/package.deb}}`

- Display the program version:

`gdebi --version`

- Do not show progress information:

`gdebi {{package.deb}} -q`

- Set an APT configuration option:

`gdebi {{package.deb}} -o {{APT_OPTS}}`

- Use alternative root dir:

`gdebi {{package.deb}} root=ROOTDIR`
