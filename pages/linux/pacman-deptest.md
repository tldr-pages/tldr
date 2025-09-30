# pacman --deptest

> Check each dependency specified and return a list of dependencies that are not currently satisfied on the system.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Print the package names of the dependencies that are not installed:

`pacman -T {{package1 package2 ...}}`

- Check if the installed package satisfies the given minimum version:

`pacman -T "{{bash>=5}}"`

- Check if a later version of a package is installed:

`pacman -T "{{bash>5}}"`

- Display [h]elp:

`pacman -Th`
