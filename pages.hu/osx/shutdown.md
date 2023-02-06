# shutdown

> A rendszer leállítása és újraindítása. További információ: <https://ss64.com/osx/shutdown.html>.

- Azonnali kikapcsolás (leállítás):

`shutdown -h now`

- Azonnali alvás:

`shutdown -s now`

- Azonnali újraindítás:

`shutdown -r now`

- Újraindítás 5 perc múlva:

`shutdown -r "+{{5}}"`

- Kikapcsolás (leállítás) 13:00 órakor (24 órás órát használ):

`shutdown -h {{1300}}`

- Újraindítás 2042. május 10-én 11:30-kor (beviteli formátum: YYMMDDHHMM):

`shutdown -r {{4205101130}}`
