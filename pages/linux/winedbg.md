# winedbg

> The Wine debugger, for debugging Windows and Winelib applications.
> More information: <https://manned.org/winedbg>.

- Launch a program under the debugger:

`winedbg {{path\to\program.exe}}`

- Attach to an already-running process by its PID:

`winedbg {{process_id}}`

- Debug a program through a gdb proxy (drive it from gdb):

`winedbg --gdb {{path\to\program.exe}}`

- Load and inspect a minidump crash file:

`winedbg {{path\to\crash.mdmp}}`

- Display help:

`winedbg --help`
