# unhash

> Verwijder gehashte locaties van uitvoerbare bestanden.
> Zie ook: `hash`.
> Meer informatie: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Verwijder een specifiek commando uit de hashtabel:

`unhash {{commando}}`

- Unhash niet-suffix [a]liassen:

`unhash -a {{alias}}`

- Unhash [s]uffix-aliassen:

`unhash -s {{alias}}`

- Unhash shell[f]uncties:

`unhash -f {{functie}}`

- Unhash [d]irectories:

`unhash -d {{map}}`

- Unhash elke functie die overeenkomt met een [m]atchend patroon:

`unhash -f -m "{{patroon}}"`
