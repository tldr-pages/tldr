# write

> Schrijf een bericht naar de terminal van een opgegeven ingelogde gebruiker (`<Ctrl c>` om te stoppen met het schrijven van berichten).
> Gebruik het `who`-commando om alle terminal-ID's van alle actieve gebruikers op het systeem te vinden.
> Zie ook: `mesg`.
> Meer informatie: <https://manned.org/write.1p>.

- Verstuur een bericht naar een gegeven gebruiker op een gegeven terminal-ID:

`write {{gebruikersnaam}} {{terminal_id}}`

- Verstuur een bericht naar "testuser" op terminal `/dev/tty/5`:

`write {{testuser}} {{tty/5}}`

- Verstuur een bericht naar "johndoe" op pseudo-terminal `/dev/pts/5`:

`write {{johndoe}} {{pts/5}}`
