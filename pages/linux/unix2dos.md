# unix2dos

> Change Unix-style line endings to DOS-style.
> Replaces LF with CRLF.
> See also `unix2mac`, `dos2unix`, and `mac2unix`.
> More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2dos {{path/to/file}}`

- Create a copy with DOS-style line endings:

`unix2dos -n {{path/to/file}} {{path/to/new_file}}`

- Display file information:

`unix2dos -i {{path/to/file}}`

- Keep/add/remove Byte Order Mark:

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
