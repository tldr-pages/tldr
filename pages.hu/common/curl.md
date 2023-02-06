# curl

> Adatátvitel egy szerverről vagy egy szerverre. Támogatja a legtöbb protokollt, beleértve a HTTP, FTP és POP3 protokollokat. További információ: <https://curl.se>.

- Letölti egy URL tartalmát egy fájlba:

`curl {{http://example.com}} --output {{path/to/file}}`

- Letölt egy fájlt, a kimenetet az URL által megadott fájlnév alá mentve:

`curl --remote-name {{http://example.com/filename}}`

- Letölt egy fájlt, követve a hely átirányítását, és automatikusan folytatja (folytatja) a korábbi fájlátvitelt, és szerverhiba esetén hibát ad vissza:

`curl --fail --remote-name --location --continue-at - {{http://example.com/filename}}`

- Formulakódolt adatok küldése ( `application/x-www-form-urlencoded` típusú POST-kérelem). Használja a `--data @file_name` vagy a `--data @'-'` címet az STDIN-ről való olvasáshoz:

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- Küldjön kérést egy extra fejléccel, egyéni HTTP-módszerrel:

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- Adatok küldése JSON formátumban, a megfelelő content-type fejléc megadásával:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Adjon meg egy felhasználónevet és jelszót a kiszolgáló hitelesítéséhez:

`curl --user myusername:mypassword {{http://example.com}}`

- Ügyféltanúsítvány és kulcs átadása egy erőforráshoz, a tanúsítvány érvényesítésének kihagyásával:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
