# bleachbit_console

> Verwijder overbodige bestanden op het bestandssysteem.
> Meer informatie: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start de grafische gebruikersinterface (GUI) van Bleachbit:

`bleachbit_console.exe --gui`

- Versnipper een bestand:

`bleachbit_console.exe --shred {{pad/naar/bestand}}`

- Toon beschikbare schoonmaakopties:

`bleachbit_console.exe --list-cleaners`

- Bekijk een voorbeeld van de bestanden die zullen worden verwijderd en andere wijzigingen voordat de schoonmaak-operatie wordt uitgevoerd:

`bleachbit_console.exe --preview {{cleaner1.optie1 cleaner2.* ...}}`

- Voer de schoonmaakoperatie uit en verwijder bestanden:

`bleachbit_console.exe --clean {{cleaner1.optie1 cleaner2.* ...}}`

- Selecteer dezelfde opties als in de GUI en voeg er meer aan toe:

`bleachbit_console.exe --preview --preset {{cleaner1.optie1 cleaner2.* ...}}`
