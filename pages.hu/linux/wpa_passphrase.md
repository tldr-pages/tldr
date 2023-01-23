# wpa_passphrase

> WPA-PSK kulcs generálása egy ASCII jelszóból egy adott SSID-hez. További információ: <https://manned.org/wpa_passphrase.1>.

- A WPA-PSK kulcs kiszámítása és megjelenítése egy adott SSID-hez a jelszó beolvasásával a `stdin` oldalon:

`wpa_passphrase {{SSID}}`

- WPA-PSK kulcs kiszámítása és megjelenítése egy adott SSID-hez a jelszótagot argumentumként megadva:

`wpa_passphrase {{SSID}} {{passphrase}}`
