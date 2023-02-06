# crontab

> Ütemezze a cron munkákat az aktuális felhasználó számára egy adott időintervallumban történő futtatásra. További információ: <https://crontab.guru/>.

- Szerkessze a crontab fájlt az aktuális felhasználóhoz:

`crontab -e`

- A crontab fájl szerkesztése egy adott felhasználó számára:

`sudo crontab -e -u {{user}}`

- Az aktuális crontab fájl cseréje a megadott fájl tartalmára:

`crontab {{path/to/file}}`

- Az aktuális felhasználó meglévő cron munkáinak listájának megtekintése:

`crontab -l`

- Az aktuális felhasználó összes cron munkájának eltávolítása:

`crontab -r`

- (\* tetszőleges értéket jelent):

`0 10 * * * {{command_to_execute}}`

- Minta crontab bejegyzés, amely 10 percenként futtat egy parancsot:

`*/10 * * * * {{command_to_execute}}`

- Minta crontab bejegyzés, amely minden pénteken 02:30-kor lefuttat egy bizonyos szkriptet:

`30 2 * * Fri {{/absolute/path/to/script.sh}}`
