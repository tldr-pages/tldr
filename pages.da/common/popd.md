# popd

> Fjern en mappe placeret på mappe-stakken via den indbyggede shell-kommando `pushd`.
> Se `pushd` for at placere en mappe på mappe-stakken og `dirs` for at vise indholdet af mappe-stakken.
> Mere information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Fjern den øverste mappe fra mappe-stakken og `cd` til mappen:

`popd`

- Fjern den N'te mappe (starter fra 0 fra venstre i den liste `dirs` printer):

`popd +N`

- Fjern den N'te mappe (starter fra 0 fra højre fra i liste `dirs` printer):

`popd -N`
