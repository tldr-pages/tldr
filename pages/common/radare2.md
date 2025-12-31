# radare2

> A set of reverse engineering tools.
> More information: <https://book.rada.re/first_steps/commandline_flags.html>.

- Open a file in write mode without parsing the file format headers:

`radare2 -nw {{path/to/binary}}`

- Debug a program:

`radare2 -d {{path/to/binary}}`

- Run a script before entering the interactive CLI:

`radare2 -i {{path/to/script.r2}} {{path/to/binary}}`

- [Interactive] Display help text for any command:

`{{radare2_command}}?`

- [Interactive] Run a shell command from the interactive CLI:

`!{{shell_command}}`

- [Interactive] Dump raw bytes of current block to a file:

`pr > {{path/to/file.bin}}`
