# gdb

> The GNU Debugger.
> More information: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Debug an executable:

`gdb {{path/to/executable}}`

- Attach a process to `gdb`:

`gdb {{[-p|--pid]}} {{procID}}`

- Debug with a core file:

`gdb {{[-c|--core]}} {{path/to/core}} {{path/to/executable}}`

- Execute given GDB commands upon start:

`gdb {{[-ex|--eval-command]}} "{{commands}}" {{path/to/executable}}`

- Start `gdb` and pass arguments to the executable:

`gdb --args {{path/to/executable}} {{argument1 argument2 ...}}`

- Skip `debuginfod` and pagination prompts and then print the backtrace:

`gdb {{[-c|--core]}} {{path/to/core}} {{path/to/executable}} -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt`
