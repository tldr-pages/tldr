# deborphan

> Display orphan packages on Debian-based OSes.
> More information: <https://manpages.debian.org/bullseye/deborphan/deborphan.1.en.html>.

- Display library packages (from the "libs" section of the package repository) that are not required by another package:

`deborphan`

- Also try to find orphaned libraries based on their name:

`deborphan --guess-all`

- Consider that a package is orphaned when it is only recommended or suggested (but not required) by another package:

`deborphan --nice-mode`
