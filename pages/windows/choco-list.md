# choco list

> Display a list of locally installed packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/list/>.

- List locally installed packages:

`choco list`

- List installed packages including system programs:

`choco list {{[-i|--include-programs]}}`

- List only the IDs of installed packages:

`choco list --id-only`

- List installed packages matching a name exactly:

`choco list {{package}} {{[-e|--exact]}}`

- List installed packages starting with a specific prefix:

`choco list --id-starts-with {{prefix}}`

- List installed packages from a specific alternative source:

`choco list {{[-s|--source]}} {{windowsfeatures|ruby|cygwin|...}}`
