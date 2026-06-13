# mimikatz kerberos

> Interagisce con i ticket Kerberos.
> Maggiori informazioni: <https://github.com/gentilkiwi/mimikatz>.

- Elenca i ticket Kerberos correnti:

`mimikatz "kerberos::list"`

- Rimuove tutti i ticket Kerberos:

`mimikatz "kerberos::purge"`

- Inietta un ticket da un file `.kirbi`:

`mimikatz "kerberos::ptt ticket.kirbi"`
