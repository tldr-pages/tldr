# expac

> A data extraction tool for alpm databases, offering printf-like flexibility for pacman-based utilities.
> See also: `pacman`.
> More information: <https://github.com/falconindy/expac>.

- List the dependencies of a package:

`expac -S '%D' {{package}}`

- List the optional dependencies of a package:

`expac -S "%o" {{package}}`

- List the download size of packages in MiB:

`expac -S -H M '%k\t%n' {{package1 package2 ...}}`

- List packages marked for upgrade with their download size:

`expac -S -H M '%k\t%n' $(pacman -Qqu) | sort -sh`

- List explicitly-installed packages with their optional dependencies:

`expac -d '\n\n' -l '\n\t' -Q '%n\n\t%O' $(pacman -Qeq)`
