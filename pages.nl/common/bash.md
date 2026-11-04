# bash

> Bourne-Again SHell, `sh`-ondersteunende commandoregel-interpreteerder.
> Zie ook: `zsh`, `!`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

- Start een interactieve shellsessie:

`bash`

- Start een interactieve shellsessie zonder het laden van startup configuratie:

`bash --norc`

- Voer een [c]ommando uit:

`bash -c "{{echo 'bash is executed'}}"`

- Voer commando's van bestand uit:

`bash {{pad/naar/script.sh}}`

- Voer commando's van bestand uit ([x]), en print elk commando voordat het wordt uitgevoerd:

`bash -x {{pad/naar/script.sh}}`

- Voer commando's van bestand uit, en stop bij de [e]erste fout:

`bash -e {{pad/naar/script.sh}}`

- Voer commando's van `stdin` uit:

`{{echo "echo 'bash is executed'"}} | bash`

- Start een bepe[r]kte shellsessie:

`bash {{[-r|--restricted]}}`
