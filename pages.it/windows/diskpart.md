# diskpart

> Gestore di dischi, volumi e partizioni.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Esegui diskpart da solo in un prompt dei comandi da amministratore per inserire la sua riga di comando:

`diskpart`

- [Interattivo] Elenca tutti i dischi:

`list disk`

- [Interattivo] Seleziona un volume:

`select volume {{volume}}`

- [Interattivo] Assegna una lettera di unità al volume selezionato:

`assign letter {{lettera}}`

- [Interattivo] Crea una nuova partizione:

`create partition primary`

- [Interattivo] Attiva il volume selezionato:

`active`

- [Interattivo] Esci da diskpart:

`exit`
