# pico

> Text editor styled after the Alpine Composer.
> More information: <https://manned.org/pico>.

- Start the editor:

`pico {{path/to/file}}`

- Start the editor with the cursor located n lines into the file:

`pico +{{n}} {{path/to/file}}`

- Start the editor with the cursor shown before the current selection:

`pico -g {{path/to/file}}`

- Define the quote string for files such as email:

`pico -Q "{{quotestring}}" {{path/to/file}}`

- Enable mouse functionality when run within an `xterm` window:

`pico -m {{path/to/file}}`

- Set the operating directory for `pico`:

`pico -o {{path/to/directory}}`

- Enable "view only" mode, which disallows any edits:

`pico -v {{path/to/file}}`

- Display all files including those beginning with a period:

`pico -a`
