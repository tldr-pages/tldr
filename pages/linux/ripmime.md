# ripmime

> Extract attachments out of a MIME encoded email package.
> More information: <https://pldaniels.com/ripmime>.

- Extract file contents in the current directory:

`ripmime -i {{path/to/file}}`

- Extract file contents in a specific directory:

`ripmime -i {{path/to/file}} -d {{path/to/directory}}`

- Extract file contents and print verbose output:

`ripmime -i {{path/to/file}} -v`

- Get detailed information about the whole decoding process:

`ripmime -i {{path/to/file}} --debug`
