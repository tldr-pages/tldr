# unix2mac

> Change Unix-style line endings to macOS-style.
> Replaces LF with CR.
> See also: `unix2dos`, `dos2unix`, `mac2unix`.
> More information: <https://manned.org/unix2mac>.

- Change the line endings of a file:

`unix2mac {{path/to/file}}`

- Create a copy with macOS-style line endings:

`unix2mac {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- Display file information:

`unix2mac {{[-i|--info]}} {{path/to/file}}`

- Keep/add/remove Byte Order Mark:

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
