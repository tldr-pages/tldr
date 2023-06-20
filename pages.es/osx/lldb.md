# lldb

> El depurador de bajo nivel LLVM.
> Más información: <https://lldb.llvm.org/man/lldb.html>.

- Depura un ejecutable:

`lldb "{{ejecutable}}"`

- Adjunta `lldb` a un proceso en ejecución con un PID dado:

`lldb -p {{pid}}`

- Espera a que se inicie un nuevo proceso con un nombre determinado y adjuntarlo al mismo:

`lldb -w -n "{{nombre_proceso}}"`
