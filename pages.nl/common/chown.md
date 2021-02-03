# chown

> Verander gebruiker- en groepsbeheer van bestanden en mappen.

- Verander gebruikkersbeheerder van een bestand/map:

`chown {{gebruiker}} {{pad/naar/bestand_of_map}}`

- Verander de gebruikersbeheerder en -groep van een bestand of map:

`chown {{gebruiker}}:{{groep}} {{pad/naar/bestand_of_map}}`

- Verander recursief de beheerder van een map en alle inhoud:

`chown -R {{gebruiker}} {{pad/naar/bestand_of_map}}`

- Verander de gebruiker van een symbolische link:

`chown -h {{gebruiker}} {{pad/naar/symlink}}`

- Verander de beheerder van een bestand of map naar dezelfde als een referentiebestand:

`chown --reference={{pad/naar/referentiebestand}} {{pad/naar/bestand_of_map}}`
