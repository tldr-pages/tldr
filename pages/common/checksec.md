# checksec

> Check security properties of executables.
> More information: <https://manned.org/checksec>.

- List security properties of an executable binary file:

`checksec --file={{path/to/binary}}`

- List security properties recursively of all executable files in a directory:

`checksec --dir={{path/to/directory}}`

- List security properties of a process:

`checksec --proc={{pid}}`

- List security properties of the running kernel:

`checksec --kernel`
