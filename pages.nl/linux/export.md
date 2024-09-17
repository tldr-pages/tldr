# export

> Exporteer shellvariabelen naar child-processen.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Stel een omgevingsvariabele in:

`export {{VARIABELE}}={{waarde}}`

- Zet een omgevingsvariabele uit:

`export -n {{VARIABELE}}`

- Exporteer een functie naar child-processen:

`export -f {{FUNCTIE_NAAM}}`

- Voeg een pad toe aan de omgevingsvariabele `PATH`:

`export PATH=$PATH:{{pad/om/toe_te_voegen}}`

- Toon een lijst van actieve geëxporteerde variabelen in shell-opdrachtvorm:

`export -p`
