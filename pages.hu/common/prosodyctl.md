# prosodyctl

> A Prosody XMPP szerver vezérlőeszköze. További információ: <https://prosody.im/doc/prosodyctl>.

- A Prosody kiszolgáló állapotának megjelenítése:

`sudo prosodyctl status`

- A kiszolgáló konfigurációs fájljainak újratöltése:

`sudo prosodyctl reload`

- Felhasználó hozzáadása a Prosody XMPP-kiszolgálóhoz:

`sudo prosodyctl adduser {{user@example.com}}`

- Felhasználó jelszavának beállítása:

`sudo prosodyctl passwd {{user@example.com}}`

- Egy felhasználó végleges törlése:

`sudo prosodyctl deluser {{user@example.com}}`
