# in-toto-record

> Create a signed link metadata file to provide evidence for supply chain steps.
> More information: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- Start the record (creates a preliminary link file):

`in-toto-record start -n {{edit-files}} -k {{path/to/key_file}} -m {{.}}`

- Stop the record (expects a preliminary link file):

`in-toto-record stop -n {{edit-files}} -k {{path/to/key_file}} -p {{.}}`
