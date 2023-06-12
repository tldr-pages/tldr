# mount

> Montare le condivisioni di rete del Network File System (NFS).
> Maggiori informazioni: <https://learn.microsoft.com/it-it/windows-server/administration/windows-commands/mount>.

- Monta una share con la lettera di unità "Z":

`mount \\{{computer_name}}\{{share_name}} {{Z:}}`

- Monta una share con la successiva lettera di unità disponibile:

`mount \\{{computer_name}}\{{share_name}} *`

- Monta una share con un timeout di lettura in secondi (predefinito a 0,8, può essere 0,9 o da 1 a 60):

`mount -o timeout={{seconds}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Monta una share e riprova fino a 10 volte se fallisce:

`mount -o retry={{retries}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Monta una share forzando la distinzione tra maiuscole e minuscole:

`mount -o casesensitive \\{{computer_name}}\{{share_name}} {{Z:}}`

- Monta una share come utente anonimo:

`mount -o anon \\{{computer_name}}\{{share_name}} {{Z:}}`

- Monta una share utilizzando un tipo di montaggio specifico:

`mount -o mtype={{soft|hard}} \\{{computer_name}}\{{share_name}} {{Z:}}`
