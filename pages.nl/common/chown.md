# chown

> Verander de eigenaar en groep van bestanden en mappen.
> Zie ook: `chgrp`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Verander de eigenaar van een bestand/map:

`sudo chown {{gebruiker}} {{pad/naar/bestand_of_map}}`

- Verander de eigenaar en groep van een bestand of map:

`sudo chown {{gebruiker}}:{{groep}} {{pad/naar/bestand_of_map}}`

- Verander de eigenaar en groep zodat beiden de naam `user` krijgen:

`sudo chown {{user}}: {{pad/naar/bestand_of_map}}`

- Verander de groep van een bestand naar een groep waar de huidige gebruiker toe behoort:

`chown :{{groep}} {{pad/naar/bestand_of_map}}`

- Verander recursief de eigenaar van een map en alle inhoud:

`sudo chown {{[-R|--recursive]}} {{gebruiker}} {{pad/naar/map}}`

- Verander de eigenaar van een symbolische link:

`sudo chown {{[-h|--no-dereference]}} {{gebruiker}} {{pad/naar/symlink}}`

- Verander de eigenaar van een bestand of map naar dezelfde als een referentiebestand:

`sudo chown --reference {{pad/naar/referentiebestand}} {{pad/naar/bestand_of_map}}`
