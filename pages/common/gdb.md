# gdb

> The GNU Debugger.
> More information: <https://www.gnu.org/software/gdb>.

- Debug an executable:

`gdb {{path/to/executable}}`

- Attach a process to gdb:

`gdb -p {{procID}}`

- Debug with a core file:

`gdb -c {{core}} {{path/to/executable}}`

- Execute given GDB commands upon start:

`gdb -ex "{{commands}}" {{path/to/executable}}`

- Start gdb and pass arguments to the executable:

`gdb --args {{path/to/executable}} {{argument1 argument2 ...}}`
