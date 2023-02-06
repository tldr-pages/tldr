# wpscan

> WordPress sebezhetőségi szkenner. További információ: <https://github.com/wpscanteam/wpscan>.

- A sebezhetőségi adatbázis frissítése:

`wpscan --update`

- Egy WordPress webhely vizsgálata:

`wpscan --url {{url}}`

- Egy WordPress-weboldal vizsgálata véletlenszerű felhasználói ügynökök és passzív észlelés segítségével:

`wpscan --url {{url}} --stealthy`

- Egy WordPress webhely vizsgálata, a sebezhető bővítmények ellenőrzése és a `wp-content` könyvtár elérési útvonalának megadása:

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}`

- WordPress-weboldal vizsgálata proxy-n keresztül:

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}`

- Felhasználói azonosítók számbavétele egy WordPress-weboldalon:

`wpscan --url {{url}} --enumerate {{u}}`

- Jelszó kitalálós támadás végrehajtása egy WordPress-weboldalon:

`wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}`

- Egy WordPress-weboldal vizsgálata, sebezhetőségi adatok gyűjtése a WPVulnDB-ből (https://wpvulndb.com/):

`wpscan --url {{url}} --api-token {{token}}`
