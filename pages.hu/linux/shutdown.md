# shutdown

> A rendszer leállítása és újraindítása. További információ: <https://manned.org/shutdown.8>.

- Azonnali kikapcsolás (leállítás):

`shutdown -h now`

- Azonnali újraindítás:

`shutdown -r now`

- Újraindítás 5 perc múlva:

`shutdown -r +{{5}} &`

- Kikapcsolás 13:00 órakor (24 órás órát használ):

`shutdown -h 13:00`

- Függőben lévő leállítási/újraindítási művelet törlése:

`shutdown -c`
