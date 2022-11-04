# pkcon

> Command line client for PackageKit console program used by Discover and Gnome software and alternative to 'apt'. 
> Mostly used by Plasma based desktop environments such as KDE Neon and Kubuntu although it is distro-agnostic.
> More information: <https://manpages.ubuntu.com/manpages/bionic/man1/pkcon.1.html>.

- Install a package:

`pkcon install {{package}}`

- Remove a package:

`pkcon remove {{package}}`

- Refresh the package cache (similar to `sudo apt update`):

`pkcon refresh`

- Update packages:

`pkcon update`

- Search for a specific package:

`pkcon search {{package}}`

- List all available packages:

`pkcon get-packages`
