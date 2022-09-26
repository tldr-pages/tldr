# echo

> Drukt gegeven argumenten af.
> Meer informatie: <https://www.gnu.org/software/coreutils/echo>.

- Druk een tekstbericht af. Let op: aanhalingstekens zijn optimaal:

`echo "{{Hallo Wereld}}"`

- Druk een bericht af met omgevingsvariabelen:

`echo "{{Mijn pad is $PATH}}"`

- Drukt een bericht af zonder te volgen met een nieuwe regel:

`echo -n "{{Hallo Wereld}}"`

- Voeg een bericht aan een bestand toe:

`echo "{{Hallo Wereld}}" >> {{bestand.txt}}`

- Schakel interpretatie van backslash ontkoming in (speciale karakters):

`echo -e "{{kolom 1\kolom 2}}"`
