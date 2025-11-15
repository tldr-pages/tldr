# checksec

> Check security properties of executables.
> More information: <https://github.com/slimm609/checksec.sh>.

- List security properties of an executable binary file:

`checksec --file={{path/to/binary}}`

- List security properties recursively of all executable files in a directory:

`checksec --dir={{path/to/directory}}`

- List security properties of a process:

`checksec --proc={{pid}}`

- List security properties of the running kernel:

`checksec --kernel`
