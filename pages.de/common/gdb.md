# gdb

> Der GNU Debugger.
> Weitere Informationen: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Debugge eine ausführbare Datei:

`gdb {{ausführbare_datei}}`

- Binde einen Prozess an gdb:

`gdb {{[-p|--pid]}} {{prozess_ID}}`

- Debugge mit einer Kerndatei:

`gdb {{[-c|--core]}} {{kerndatei}} {{ausführbare_datei}}`

- Führe angegebene Befehle beim Start von gdb aus:

`gdb {{[-ex|--eval-command]}} "{{befehle}}" {{ausführbare_datei}}`

- Starte gdb und übergib Argumente an die ausführbare Datei:

`gdb --args {{ausführbare_datei}} {{argument1}} {{argument2}}`
