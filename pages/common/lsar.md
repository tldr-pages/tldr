# lsar

> List archive file contents.
> See also: `unar`, `ar`.
> More information: <https://manned.org/lsar>.

- List archive file contents:

`lsar {{archive}}`

- List password protected archive file contents:
`lsar {{archive}} --password {{password}}`

- Print al[L] available information about each file in the archive (it's very long):

`lsar {{-L|--verylong}} {{archive}}`

- Test the integrity of the files in the archive (if possible):

`lsar --test {{archive}}`

- List archive file contents in JSON format:

`lsar --json {{archive}}`

- Display help information:

`lsar --help`
