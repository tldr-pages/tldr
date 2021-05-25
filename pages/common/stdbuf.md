# stdbuf

> Run a command with modified buffering operations for its standard streams.
> More information: <https://www.gnu.org/software/coreutils/stdbuf>.

- Change the standard input buffer size to 512 KiB:

`stdbuf --input={{512K}} {{command}}`

- Change the standard output buffer to line-buffered:

`stdbuf --output={{L}} {{command}}`

- Change the standard error buffer to unbuffered:

`stdbuf --error={{0}} {{command}}`
