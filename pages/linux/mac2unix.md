# mac2unix

> Change macOS-style line endings to Unix-style.
> Replaces CR with LF.
> See also `unix2dos`, `unix2mac`, and `dos2unix`.
> More information: <https://manned.org/mac2unix>.

- Change the line endings of a file:

`mac2unix {{path/to/file}}`

- Create a copy with Unix-style line endings:

`mac2unix {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- Display file information:

`mac2unix {{[-i|--info]}} {{path/to/file}}`

- Keep/add/remove Byte Order Mark:

`mac2unix --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
