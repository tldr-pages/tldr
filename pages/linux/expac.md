# expac

> A data extraction tool for alpm databases, offering printf-like flexibility for pacman-based utilities.
> See also: `pacman`.
> More information: <https://github.com/falconindy/expac#name>.

- List the dependencies of a package:

`expac {{[-S|--sync]}} '%D' {{package}}`

- List the optional dependencies of a package:

`expac {{[-S|--sync]}} "%o" {{package}}`

- List the download size of packages in MiB:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' {{package1 package2 ...}}`

- List packages marked for upgrade with their download size:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' $(pacman -Qqu) | sort {{[-sh|--sort --human-numeric-sort]}}`

- List explicitly-installed packages with their optional dependencies:

`expac {{[-d|--delim]}} '\n\n' {{[-l|--listdelim]}} '\n\t' {{[-Q|--query]}} '%n\n\t%O' $(pacman -Qeq)`
