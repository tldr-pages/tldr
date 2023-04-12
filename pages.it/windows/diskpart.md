# diskpart

> Gestore di dischi, volumi e partizioni.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Esegui diskpart da solo in un prompt dei comandi da amministratore per inserire la sua riga di comando:

`diskpart`

- Elenca tutti i dischi:

`list disk`

- Seleziona un volume:

`select volume {{volume}}`

- Assegna una lettera di unità al volume selezionato:

`assign letter {{lettera}}`

- Crea una nuova partizione:

`create partition primary`

- Attiva il volume selezionato:

`active`

- Esci da diskpart:

`exit`
