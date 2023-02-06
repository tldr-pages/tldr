# roll

> Egy felhasználó által meghatározott kockasorozatot dob. További információ: <https://manned.org/roll>.

- Dobjon 3 6 oldalú kockával és összegezze az eredményeket:

`roll {{3d}}`

- Dobjon 1 8 oldalú kockát, adjon össze 3 kockát és összegezze az eredményeket:

`roll {{d8 + 3}}`

- Dobjon 4 6 oldalú kockával, tartsa meg a 3 legmagasabb eredményt, és összegezze az eredményeket:

`roll {{4d6h3}}`

- Dobj 2 12 oldalú kockát kétszer, és mutasd meg minden dobást:

`roll --verbose {{2{2d12}}}`

- Dobj 2 20 oldalú kockával, amíg az eredmény nagyobb nem lesz 10-nél:

`roll "{{2d20>10}}"`

- Dobjon 2 5 oldalú kockával 3-szor, és mutassa meg a végeredményt:

`roll --sum-series {{3{2d5}}}`
