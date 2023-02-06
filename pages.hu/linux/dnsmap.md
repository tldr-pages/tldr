# dnsmap

> A dnsmap parancs egy tartományt vizsgál át a közös aldomainek után, pl. smtp.domain.org. További információ: <https://github.com/resurrecting-open-source-projects/dnsmap>.

- Aldomainek keresése a belső szólista segítségével:

`dnsmap {{example.com}}`

- Adja meg az ellenőrizendő aldomainek listáját:

`dnsmap {{example.com}} -w {{path/to/wordlist.txt}}`

- Az eredmények tárolása CSV-fájlba:

`dnsmap {{example.com}} -c {{path/to/file.csv}}`

- 2 téves pozitív IP figyelmen kívül hagyása (legfeljebb 5 lehetséges):

`dnsmap {{example.com}} -i {{123.45.67.89,98.76.54.32}}`
