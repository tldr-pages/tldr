# chown

> Verander gebruiker- en groepsbeheer van bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Verander de gebruikersbeheerder van een bestand/map:

`sudo chown {{gebruiker}} {{pad/naar/bestand_of_map}}`

- Verander de gebruikersbeheerder en -groep van een bestand of map:

`sudo chown {{gebruiker}}:{{groep}} {{pad/naar/bestand_of_map}}`

- Verander de gebruikersbeheerder en -groep zodat beiden de naam `user` krijgen:

`sudo chown {{user}}: {{pad/naar/bestand_of_map}}`

- Verander recursief de beheerder van een map en alle inhoud:

`sudo chown {{[-R|--recursive]}} {{gebruiker}} {{pad/naar/bestand_of_map}}`

- Verander de gebruiker van een symbolische link:

`sudo chown {{[-h|--no-dereference]}} {{gebruiker}} {{pad/naar/symlink}}`

- Verander de beheerder van een bestand of map naar dezelfde als een referentiebestand:

`sudo chown --reference {{pad/naar/referentiebestand}} {{pad/naar/bestand_of_map}}`
