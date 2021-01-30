# gdebi

> Simple tool to install deb files.
> More information: <https://launchpad.net/gdebi>.

- Install local deb packages resolving and installing its dependencies:

`gdebi {{package.deb}}`

- Display the program version:

`gdebi --version`

- Do not show progress information:

`gdebi -q`

- Set an APT configuration option:

`gdebi -o {{APT_OPTS}}`

- Use alternative root dir:

`gdebi root=ROOTDIR`
