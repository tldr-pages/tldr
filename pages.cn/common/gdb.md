# gdb

> The GNU Debugger.

- Debug an executable:

`gdb {{executable}}`

- Attach a process to gdb:

`gdb -p {{procID}}`

- Execute given GDB commands upon start:

`gdb -ex "{{commands}}" {{executable}}`

- Start gdb and pass arguments:

`gdb --args {{executable}} {{argument1}} {{argument2}}`
