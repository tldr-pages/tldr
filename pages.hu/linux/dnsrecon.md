# dnsrecon

> DNS-felszámoló eszköz. További információ: <https://github.com/darkoperator/dnsrecon>.

- Egy tartomány beolvasása és az eredmények mentése egy SQLite adatbázisba:

`dnsrecon --domain {{example.com}} --db {{path/to/database.sqlite}}`

- Egy tartomány beolvasása, a névszerver megadása és a zóna átvitele:

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- Egy tartomány átvizsgálása, nyers erővel végrehajtott támadás és az aldomainek és hosztnevek szótárának felhasználásával:

`dnsrecon --domain {{example.com}} --dictionary {{path/to/dictionary.txt}} --type brt`

- Egy tartomány beolvasása, az SPF rekordból származó IP-tartományok fordított keresése és az eredmények JSON fájlba mentése:

`dnsrecon --domain {{example.com}} -s --json`

- Egy tartomány átvizsgálása, Google-felszámolás elvégzése és az eredmények CSV-fájlba mentése:

`dnsrecon --domain {{example.com}} -g --csv`

- Egy tartomány beolvasása, DNS cache snooping végrehajtása:

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{path/to/dictionary.txt}}`

- Egy tartomány beolvasása, zónaséta végrehajtása:

`dnsrecon --domain {{example.com}} --type zonewalk`
