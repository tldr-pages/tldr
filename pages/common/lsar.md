# lsar

> List an archive file's contents.
> See also: `unar`, `ar`.
> More information: <https://manned.org/lsar>.

- List an archive file's contents:

`lsar {{path/to/archive}}`

- List a password protected archive file's contents:

`lsar {{path/to/archive}} {{[-p|--password]}} {{password}}`

- Print all available information about each file in the archive (it's very long):

`lsar {{[-L|--verylong]}} {{path/to/archive}}`

- Test the integrity of the files in the archive (if possible):

`lsar {{[-t|--test]}} {{path/to/archive}}`

- List the archive file's contents in JSON format:

`lsar {{[-j|--json]}} {{path/to/archive}}`

- Display help:

`lsar {{[-h|--help]}}`
