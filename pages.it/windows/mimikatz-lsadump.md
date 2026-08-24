# mimikatz lsadump

> Esegue il dump di segreti dalla Windows Local Security Authority (LSA).
> Richiede privilegi SYSTEM.
> Maggiori informazioni: <https://github.com/gentilkiwi/mimikatz>.

- Esegue il dump degli hash SAM:

`mimikatz "lsadump::sam"`

- Esegue il dump dei segreti dall'hive SECURITY:

`mimikatz "lsadump::secrets"`

- Esegue il dump delle credenziali di dominio memorizzate in cache:

`mimikatz "lsadump::cache"`
