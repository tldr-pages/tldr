# cut

> Schneide Felder von stdin oder einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cut>.

- Schneide bestimmte Zeichen oder einen Feldbereich jeder Zeile aus:

`{{befehl}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Schneide einen bestimmten Bereich jeder Zeile mit einem bestimmten Trennzeichen aus:

`{{befehl}} | cut --delimiter="{{,}} --{{characters}}={{1}}"`

- Schneide einen bestimmten Bereich jeder Zeile einer bestimmten Datei aus:

`cut --{{characters}}={{1}} {{pfad/zu/datei}}`
