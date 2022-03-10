# attrib

> Displays or changes file and directory attributes.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Print the attributes of all files in the current directory:

`attrib`

- Print the attributes of all files in the current directory and sub-directories recur[s]ively:

`attrib /s`

- Print the attributes of the files and directories in the current [d]irectory:

`attrib /d`

- Set the [r]ead-only/[a]rchive/[s]ystem/[h]idden attribute to a file/directory:

`attrib +{{r|a|s|h}} {{path/to/file_or_directory}}`

- Remove the [r]ead-only/[a]rchive/[s]ystem/[h]idden attribute from a file/directory:

`attrib -{{r|a|s|h}} {{path/to/file_or_directory}}`

- Set multiple attributes to a file/directory:

`attrib +r +a {{path/to/file_or_directory}}`
