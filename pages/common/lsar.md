# lsar

> List an archive file's contents.
> See also: `unar`, `ar`.
> More information: <https://manned.org/lsar>.

- List an archive file's contents:

`lsar {{path/to/archive}}`

- List a password protected archive file's contents:

`lsar {{path/to/archive}} --password {{password}}`

- Print al[L] available information about each file in the archive (it's very long):

`lsar {{-L|--verylong}} {{path/to/archive}}`

- Test the integrity of the files in the archive (if possible):

`lsar --test {{path/to/archive}}`

- List the archive file's contents in JSON format:

`lsar --json {{path/to/archive}}`

- Display help:

`lsar --help`
