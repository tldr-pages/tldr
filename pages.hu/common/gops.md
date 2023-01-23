# gops

> CLI eszköz, amely felsorolja és diagnosztizálja a rendszerben jelenleg futó Go folyamatokat. További információ: <https://github.com/google/gops>.

- A helyben futó összes Go folyamat kinyomtatása:

`gops`

- További információk nyomtatása egy folyamatról:

`gops {{pid}}`

- Folyamatfa megjelenítése:

`gops tree`

- Egy célprogram aktuális stack trace-jének kinyomtatása:

`gops stack {{pid|addr}}`

- Az aktuális futásidejű memóriastatisztika kiírása:

`gops memstats {{pid|addr}}`
