# fail2ban-client

> A fail2ban kiszolgáló konfigurálása és vezérlése. További információ: <https://github.com/fail2ban/fail2ban>.

- A jail szolgáltatás aktuális állapotának lekérdezése:

`fail2ban-client status {{jail}}`

- A megadott IP-cím eltávolítása a börtönszolgáltatás tiltólistájáról:

`fail2ban-client set {{jail}} unbanip {{ip}}`

- A fail2ban kiszolgáló életben létének ellenőrzése:

`fail2ban-client ping`
