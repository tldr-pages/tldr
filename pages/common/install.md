# install

> Copy files and set attributes.
> Typically used by Makefiles.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Copy files to the destination:

`install {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Copy files to the destination, setting their ownership:

`install {{[-o|--owner]}} {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Copy files to the destination, setting their group ownership:

`install {{[-g|--group]}} {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Copy files to the destination, setting their `mode`:

`install {{[-m|--mode]}} {{+x}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Copy files and apply access/modification times of source to the destination:

`install {{[-p|--preserve-timestamps]}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Copy files and create the directories at the destination if they don't exist:

`install -D {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`
