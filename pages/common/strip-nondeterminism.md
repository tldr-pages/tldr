# strip-nondeterminism

> Remove non-deterministic information (e.g. timestamps) from files.
> More information: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>.

- Strip nondeterministic information from a file:

`strip-nondeterminism {{path/to/file}}`

- Strip nondeterministic information from a file manually specifying the filetype:

`strip-nondeterminism --type {{filetype}} {{path/to/file}}`

- Strip nondeterministic information from a file; instead of removing timestamps set them to the specified UNIX timestamp:

`strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}`
