# lldb

> El depurador LLVM de bajo nivel.
> Más información: <https://lldb.llvm.org>.

- Depura un ejecutable:

`lldb {{ejecutable}}`

- Asocia `lldb` a un proceso de ejecución con un PID dado:

`lldb -p {{pid}}`

- Espera un nuevo proceso con un nombre dado para ejecutarse y asociarse al mismo:

`lldb -w -n {{nombre_del_proceso}}`
