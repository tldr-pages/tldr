# lldb

> Depanatorul LLVM de nivel scăzut.
> Mai multe informaţii: <https://lldb.llvm.org>

- Depanarea unui executabil:

`lldb {{executable}}`

- Atașați `lldb` la un proces de funcționare cu un PID dat:

`lldb -p {{pid}}`

- Așteptați un nou proces de lansare cu un nume dat și atașați-l:

`lldb -w -n {{process_name}}`
