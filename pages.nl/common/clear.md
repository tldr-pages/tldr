# clear

> Leegt het scherm van de terminal.
> Meer informatie: <https://manned.org/clear>.

- Maak het scherm leeg (gelijk aan het indrukken van `<Ctrl l>` in de Bash-shell):

`clear`

- Maak het scherm leeg maar behoud de scrollbackbuffer van de terminal:

`clear -x`

- Geef het type terminal aan dat leeggemaakt moet worden (standaard ingesteld op de waarde van de omgevingsvariabele `TERM`):

`clear -T {{type_of_terminal}}`

- Toon de versie van `ncurses` die door `clear` wordt gebruikt:

`clear -V`
