# mount

> Koppel Network File System (NFS) netwerkschijven.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- Koppel een netwerkshare aan de "Z"-schijfletter:

`mount \\{{computer_naam}}\{{share_naam}} {{Z:}}`

- Koppel een netwerkshare aan de eerstvolgende beschikbare schijfletter:

`mount \\{{computer_naam}}\{{share_naam}} *`

- Koppel een netwerkshare met een leesslot in seconden (standaard 0,8, kan 0,9 of 1 tot 60 zijn):

`mount -o timeout={{seconden}} \\{{computer_naam}}\{{share_naam}} {{Z:}}`

- Koppel een netwerkshare en probeer het maximaal 10 keer opnieuw als het mislukt:

`mount -o retry=10 \\{{computer_naam}}\{{share_naam}} {{Z:}}`

- Koppel een netwerkshare met geforceerde hoofdlettergevoeligheid:

`mount -o casesensitive \\{{computer_naam}}\{{share_naam}} {{Z:}}`

- Koppel een netwerkshare als een anonieme gebruiker:

`mount -o anon \\{{computer_naam}}\{{share_naam}} {{Z:}}`

- Koppel een netwerkshare met een specifiek type koppeling:

`mount -o mtype={{soft|hard}} \\{{computer_naam}}\{{share_naam}} {{Z:}}`
