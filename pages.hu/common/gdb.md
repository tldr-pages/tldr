# gdb

> A GNU Debugger. További információ: <https://www.gnu.org/software/gdb>.

- Futtatható program hibakeresése:

`gdb {{executable}}`

- Egy folyamat csatolása a gdb-hez:

`gdb -p {{procID}}`

- Hibakeresés egy magfájllal:

`gdb -c {{core}} {{executable}}`

- Adott GDB parancsok végrehajtása indításkor:

`gdb -ex "{{commands}}" {{executable}}`

- A gdb indítása és argumentumok átadása a futtatható programnak:

`gdb --args {{executable}} {{argument1}} {{argument2}}`
