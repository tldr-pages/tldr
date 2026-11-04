# cd

> Zobrazit aktuální adresář nebo přesun do jiného adresáře.
> V PowerShellu je tento příkaz aliasem příkazu `Set-Location`. Tato dokumentace vychází z verze příkazu `cd` pro příkazový řádek (`cmd`).
> Více informací: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Zobrazit dokumentaci ekvivalentního PowerShell příkazu:

`tldr set-location`

- Zobrazit cestu k aktuálnímu adresáři:

`cd`

- Přesun do zadaného adresáře na stejném disku:

`cd {{cesta\k\adresari}}`

- Přesun do zadaného adresáře na jiném disku:

`cd /d {{C}}:{{cesta\k\adresari}}`

- Přesun do nadřazené složky aktuálního adresáře:

`cd ..`

- Přesun do domovského adresáře aktuálního uživatele:

`cd %userprofile%`

- Přesun do kořenového adresáře aktuálního disku:

`cd \`
