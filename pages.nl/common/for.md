# for

> Voer een commando meerdere keren uit.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Itereer over de command line argumenten:

`for {{variabele}}; do {{echo $variabele}}; done`

- Voer de gegeven commando's uit voor elk van de opgegeven items:

`for {{variabele}} in {{item1 item2 ...}}; do {{echo "Loop wordt uitgevoerd"}}; done`

- Itereer over een gegeven reeks nummers:

`for {{variabele}} in {{{van..tot..stap}}}; do {{echo "Loop wordt uitgevoerd"}}; done`

- Itereer over een gegeven lijst van bestanden:

`for {{variabele}} in {{pad/naar/bestand1 pad/naar/bestand2 ...}}; do {{echo "Loop wordt uitgevoerd"}}; done`

- Itereer over een gegeven lijst van directories:

`for {{variabele}} in {{pad/naar/directory1/ pad/naar/directory2/ ...}}; do {{echo "Loop wordt uitgevoerd"}}; done`

- Voer een gegeven commando uit in elke directory:

`for {{variabele}} in */; do (cd "${{variabele}}" || continue; {{echo "Loop wordt uitgevoerd"}}) done`
