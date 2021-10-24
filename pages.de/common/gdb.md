# gdb

> Der GNU Debugger.
> Weitere Informationen: <https://www.gnu.org/software/gdb>.

- Debugge eine ausführbare Datei:

`gdb {{ausführbare_datei}}`

- Binde einen Prozess an gdb:

`gdb -p {{prozess_ID}}`

- Debugge mit einer Kerndatei:

`gdb -c {{kerndatei}} {{ausführbare_datei}}`

- Führe angegebene Befehle beim Start von gdb aus:

`gdb -ex "{{befehle}}" {{ausführbare_datei}}`

- Starte gdb und übergib Argumente an die ausführbare Datei:

`gdb --args {{ausführbare_datei}} {{argument1}} {{argument2}}`
