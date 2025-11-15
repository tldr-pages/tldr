# chkdsk

> Controlla il file system e i metadata dei dischi per cercare errori.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Specifica la lettera del disco (seguita da due punti ':'), monta una partizione o un disco da controllare:

`chkdsk {{disco}}`

- Ripara gli errori di un disco specifico:

`chkdsk {{disco}} /f`

- Smonta un disco specifico prima di eseguire il controllo:

`chkdsk {{volume}} /x`

- Cambia la dimensione dei file di log in una dimensione specifica (solo per NTFS):

`chkdsk /l{{dimensione}}`
