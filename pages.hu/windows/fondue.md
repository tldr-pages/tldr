# fondue

> A Windows opcionális funkcióinak parancssori telepítője. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- Egy adott Windows-szolgáltatás engedélyezése:

`fondue /enable-feature:{{feature}}`

- Minden kimeneti üzenet elrejtése a felhasználó számára:

`fondue /enable-feature:{{feature}} /hide-ux:all`

- Hívó folyamat nevének megadása a hibajelentésekhez:

`fondue /enable-feature:{{feature}} /caller-name:{{name}}`
