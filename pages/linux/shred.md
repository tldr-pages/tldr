# shred

> Shred - overwrite a file to hide its contents, and optionally delete it

- Overwrite the specified FILE(s) repeatedly, in order to make it harder for even very expensive hardware probing to recover the data.

`shred {{file}}`

- overwrite the file with zeros

`shred -z {{file}}`

- amount of iterations

`shred -n {{iterations}} {{file}}`
