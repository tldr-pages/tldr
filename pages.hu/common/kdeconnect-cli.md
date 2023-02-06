# kdeconnect-cli

> KDE Connect CLI. További információ: <https://kdeconnect.kde.org>.

- Az összes eszköz listázása:

`kdeconnect-cli --list-devices`

- Az elérhető (párosított és elérhető) eszközök listázása:

`kdeconnect-cli --list-available`

- Párosítás kérése egy adott eszközzel, megadva annak azonosítóját:

`kdeconnect-cli --pair --device {{device_id}}`

- Egy eszköz csengetése, megadva annak nevét:

`kdeconnect-cli --ring --name "{{device_name}}"`

- URL vagy fájl megosztása egy párosított eszközzel, megadva annak azonosítóját:

`kdeconnect-cli --share {{url|path/to/file}} --device {{device_id}}`

- SMS küldése opcionális csatolmányokkal egy adott számra:

`kdeconnect-cli --name "{{device_name}}" --send-sms "{{message}}" --destination {{phone_number}} --attachment {{path/to/file}}`

- Egy adott eszköz feloldása:

`kdeconnect-cli --name "{{device_name}}" --unlock`

- Egy adott eszköz billentyűleütés szimulálása:

`kdeconnect-cli --name "{{device_name}}" --send-keys {{key}}`
