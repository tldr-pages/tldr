# unix2dos

> Change Unix-style line endings to DOS-style.
> Replaces LF with CRLF.
> See also: `unix2mac`, `dos2unix`, `mac2unix`.
> More information: <https://manned.org/unix2dos>.

- Change the line endings of a file:

`unix2dos {{path/to/file}}`

- Create a copy with DOS-style line endings:

`unix2dos {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- Display file information:

`unix2dos {{[-i|--info]}} {{path/to/file}}`

- Keep/add/remove Byte Order Mark:

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
