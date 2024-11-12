# lldb

> De LLVM Low-Level Debugger.
> Meer informatie: <https://lldb.llvm.org>.

- Debug een uitvoerbaar bestand:

`lldb {{uitvoerbaar_bestand}}`

- Koppel `lldb` aan een draaiend proces met een gegeven PID:

`lldb -p {{pid}}`

- Wacht op de start van een nieuw proces met een gegeven naam en koppel eraan:

`lldb -w -n {{proces_naam}}`
