# gdb

> O depurador GNU.
> Mais informações: <https://www.gnu.org/software/gdb>.

- Depura um executável:

`gdb {{executável}}`

- Vincula um processo ao gdb:

`gdb -p {{PID}}`

- Depura usando um arquivo de "core dump":

`gdb -c {{core}} {{executável}}`

- Executa um dado comando do gdb ao iniciar:

`gdb -ex "{{comandos}}" {{executável}}`

- Inicia o gdb passando argumentos para o executável:

`gdb --args {{executável}} {{argumento1}} {{argumento2}}`
