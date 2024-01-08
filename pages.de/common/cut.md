# cut

> Schneide Felder von `stdin` oder einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cut>.

- Schneide bestimmte Zeichen oder einen Bereich von Feldern jeder Zeile aus:

`{{befehl}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Schneide einen bestimmten Bereich von Feldern jeder Zeile mit einem bestimmten Trennzeichen aus:

`{{befehl}} | cut --delimiter="{{,}}" --fields={{1}}`

- Schneide einen bestimmten Bereich von Zeichen jeder Zeile einer bestimmten Datei aus:

`cut --characters={{1}} {{pfad/zu/datei}}`
