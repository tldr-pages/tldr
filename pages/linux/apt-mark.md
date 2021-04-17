# apt-mark

> Utility to change the status of installed packages.
> More information: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Mark a package as automatically installed:

`sudo apt-mark auto {{package_name}}`

- Hold a package at its current version and prevent updates to it:

`sudo apt-mark hold {{package_name}}`

- Allow a package to be updated again:

`sudo apt-mark unhold {{package_name}}`

- Show manually installed packages:

`apt-mark showmanual`

- Show held packages that aren't being updated:

`apt-mark showhold`
