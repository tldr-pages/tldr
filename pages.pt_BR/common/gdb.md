# gdb

> O depurador GNU.
> Mais informações: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Depura um executável:

`gdb {{executável}}`

- Vincula um processo ao gdb:

`gdb {{[-p|--pid]}} {{PID}}`

- Depura usando um arquivo de "core dump":

`gdb {{[-c|--core]}} {{core}} {{executável}}`

- Executa um dado comando do gdb ao iniciar:

`gdb {{[-ex|--eval-command]}} "{{comandos}}" {{executável}}`

- Inicia o gdb passando argumentos para o executável:

`gdb --args {{executável}} {{argumento1}} {{argumento2}}`
