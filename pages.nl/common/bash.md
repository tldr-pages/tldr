# bash

> Bourne-Again SHell.
> `sh`-ondersteunende commandoregel-interpreteerder.
> Meer informatie: <https://gnu.org/software/bash/>.

- Start interactieve shell:

`bash`

- Voer een commando uit:

`bash -c "{{commando}}"`

- Voer commando's van bestand uit:

`bash {{bestand.sh}}`

- Voer commando's van bestand uit, en print alle uitgevoerde commando's naar de terminal:

`bash -x {{bestand.sh}}`

- Voer commando's van bestand uit, en stop bij de eerste fout:

`bash -e {{bestand.sh}}`

- Voer commando's van stdin uit:

`bash -s`

- Print de versieinformatie van bash (gebruik `echo $BASH_VERSION` om alleen de versie te krijgen zonder licentie):

`bash --version`
