# debsecan

> Debian Security Analyzer, egy olyan eszköz, amely egy adott Debian telepítés sebezhetőségeit listázza. További információ: <https://gitlab.com/fweimer/debsecan>.

- Az aktuális gépen telepített sebezhető csomagok listázása:

`debsecan`

- Egy adott csomag sebezhető telepített csomagjainak listázása:

`debsecan --suite {{release_code_name}}`

- Csak a javított sebezhetőségek listázása:

`debsecan --suite {{release_code_name}} --only-fixed`

- Csak az instabil ("sid") csomagok fix sebezhetőségeit listázza, és a root-nak küldött levél:

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- A sebezhető telepített csomagok frissítése:

`sudo apt upgrade $(debsecan --only-fixed --format {{packages}})`
