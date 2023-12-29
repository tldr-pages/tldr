# bash

> Bourne-Again SHell, `sh`-ondersteunende commandoregel-interpreteerder.
> Bekijk ook: `zsh`, `histexpand` (history expansion).
> Meer informatie: <https://www.gnu.org/software/bash/>.

- Start een interactieve shell sessie:

`bash`

- Start een interactieve shell sessie zonder het laden van startup configuratie:

`bash --norc`

- Voer een [c]ommando uit:

`bash -c "{{echo 'bash is executed'}}"`

- Voer commando's van bestand uit:

`bash {{pad/naar/script.sh}}`

- Voer commando's van bestand uit, en print alle uitgevoerde commando's naar de terminal:

`bash -x {{pad/naar/script.sh}}`

- Voer commando's van bestand uit, en stop bij de eerste fout:

`bash -e {{pad/naar/script.sh}}`

- Voer commando's van `stdin` uit:

`{{echo "echo 'bash is executed'"}} | bash`

- Start een beperkte shell sessie:

`bash -r`
