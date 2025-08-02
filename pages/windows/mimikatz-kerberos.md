# mimikatz kerberos

> Interact with Kerberos tickets.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- List current Kerberos tickets:

`mimikatz "kerberos::list"`

- Purge all Kerberos tickets:

`mimikatz "kerberos::purge"`

- Inject a ticket from a `.kirbi` file:

`mimikatz "kerberos::ptt ticket.kirbi"`
