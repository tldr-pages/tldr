# choco apikey

> API-kulcsok kezelése Chocolatey forrásokhoz. További információ: <https://chocolatey.org/docs/commands-apikey>.

- A források és API-kulcsaik listájának megjelenítése:

`choco apikey`

- Egy adott forrás és API-kulcsainak megjelenítése:

`choco apikey --source "{{source_url}}"`

- API-kulcs beállítása egy forráshoz:

`choco apikey --source "{{source_url}}" --key "{{api_key}}"`

- API-kulcs eltávolítása egy forráshoz:

`choco apikey --source "{{source_url}}" --remove`
