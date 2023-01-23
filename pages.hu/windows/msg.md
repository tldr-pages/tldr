# msg

> Üzenet küldése egy adott felhasználónak vagy munkamenetnek. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Üzenet küldése egy megadott felhasználónak vagy munkamenetnek:

`msg {{username|session_name|session_id}} {{message}}`

- Üzenet küldése a `stdin` címen:

`echo "{{message}}" | msg {{username|session_name|session_id}}`

- Üzenet küldése egy adott kiszolgálónak:

`msg /server:{{server_name}} {{username|session_name|session_id}}`

- Üzenet küldése az aktuális gép összes felhasználójának:

`msg *`

- Az üzenet késleltetésének beállítása másodpercben:

`msg /time:{{seconds}}`
