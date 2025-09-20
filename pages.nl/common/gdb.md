# gdb

> De GNU Debugger.
> Meer informatie: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Debug een uitvoerbaar bestand:

`gdb {{pad/naar/uitvoerbaar_bestand}}`

- Koppel een proces aan `gdb`:

`gdb {{[-p|--pid]}} {{procID}}`

- Debug met een core-bestand:

`gdb {{[-c|--core]}} {{pad/naar/core}} {{pad/naar/uitvoerbaar_bestand}}`

- Voer een bepaald GDB-commando uit bij het starten:

`gdb {{[-ex|--eval-command]}} "{{commando's}}" {{pad/naar/uitvoerbaar_bestand}}`

- Start `gdb` en geef argumenten mee aan het uitvoerbaar bestand:

`gdb --args {{pad/naar/uitvoerbaar_bestand}} {{argument1 argument2 ...}}`

- Sla `debuginfod`- en paginationprompts over en toon de backtrace:

`gdb {{[-c|--core]}} {{pad/naar/core}} {{pad/naar/uitvoerbaar_bestand}} -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt`
