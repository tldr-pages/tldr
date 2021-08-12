# gdb

> Depanatorul GNU.
> Mai multe informaţii: <https://www.gnu.org/software/gdb>

- Depanarea unui executabil:

`gdb {{executable}}`

- Atașați un proces la gdb:

`gdb -p {{procID}}`

- Depanare cu un fișier de bază:

`gdb -c {{core}} {{executable}}`

- Executa comenzi date GDB la start:

`gdb -ex "{{commands}}" {{executable}}`

- Începeți gdb și treceți argumente executabilului:

`gdb --args {{executable}} {{argument1}} {{argument2}}`
