# dirsearch

> Webes útvonalszkenner. További információ: <https://github.com/maurosoria/dirsearch>.

- A webkiszolgáló vizsgálata a közös kiterjesztésekkel rendelkező közös elérési utakra:

`dirsearch --url {{url}} --extensions-list`

- A webkiszolgálók listájának vizsgálata a `.php` kiterjesztésű közös elérési utakra:

`dirsearch --url-list {{path/to/url-list.txt}} --extensions {{php}}`

- Webkiszolgáló vizsgálata a közös kiterjesztésű, felhasználó által meghatározott elérési utakra:

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-paths.txt}}`

- Webkiszolgáló keresése cookie használatával:

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- Webkiszolgáló vizsgálata a `HEAD` HTTP-módszer használatával:

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- Webkiszolgáló vizsgálata, az eredmények mentése a `.json` fájlba:

`dirsearch --url {{url}} --extensions {{php}} --json-report {{path/to/report.json}}`
