# echo

> Gib angegebene Argumente aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/echo>.

- Gib einen Text aus. (Hinweis: Anführungszeichen sind optional):

`echo "{{Hallo Welt}}"`

- Gib einen Text mit Umgebungsvariablen aus:

`echo "{{Liste aller Systempfade: $PATH}}"`

- Gib einen Text ohne darauffolgenden Zeilenumbruch aus:

`echo -n "{{Hallo Welt}}"`

- Füge einen Text in eine Datei ein:

`echo "{{Hallo Welt}}" >> {{datei.txt}}`

- Ermögliche Interpretation von Fluchtsymbolen (backslash escape):

`echo -e "{{Spalte 1\tSpalte 2}}"`
