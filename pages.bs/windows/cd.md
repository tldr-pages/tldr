# cd

> Prikaži trenutni radni direktorij ili pređi u drugi direktorij.
> U PowerShellu, ova komanda je pseudonim za `Set-Location`. Ova dokumentacija zasniva se na verziji naredbe `cd` iz Command Prompta (`cmd`).
> Više informacija: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Pogledajte dokumentaciju ekvivalentne PowerShell komande:

`tldr set-location`

- Pokaži put trenutnog radnog direktorija:

`cd`

- Idi u specifični direktorij na istom pogonu:

`cd {{put\do\datoteke}}`

- Idi u specifični direktorij na drugom pogonu:

`cd /d {{C}}:{{put\do\datoteke}}`

- Idi u roditeljski direktorij trenutnog direktorija:

`cd ..`

- Idi u kućni direktorij trenutnog korisnika:

`cd %userprofile%`

- Pređi na korijen trenutnog pogona:

`cd \`
