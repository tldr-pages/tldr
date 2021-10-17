# deborphan

> Display orphan packages on operating systems using the APT package manager.
> More information: <https://manpages.debian.org/latest/deborphan/deborphan.html>.

- Display library packages (from the "libs" section of the package repository) which are not required by another package:

`deborphan`

- List orphan packages from the "libs" section as well as orphan packages that have a name that looks like a library name:

`deborphan --guess-all`

- Find packages which are only recommended or suggested (but not required) by another package:

`deborphan --nice-mode`
