# bleachbit

> Verwijder overbodige bestanden op het bestandssysteem.
> Meer informatie: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start de grafische gebruikersinterface (GUI) van Bleachbit:

`bleachbit --gui`

- Versnipper een bestand:

`bleachbit --shred {{pad/naar/bestand}}`

- Toon beschikbare schoonmaakopties:

`bleachbit --list-cleaners`

- Bekijk een voorbeeld van de bestanden die zullen worden verwijderd en andere wijzigingen die worden doorgevoerd voordat de schoonmaakoperatie wordt uitgevoerd:

`bleachbit --preview {{--preset|cleaner1.option1 cleaner2.* ...}}`

- Voer de schoonmaakoperatie uit en verwijder bestanden:

`bleachbit --clean {{--preset|cleaner1.option1 cleaner2.* ...}}`
