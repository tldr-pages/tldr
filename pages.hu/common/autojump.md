# autojump

> Gyorsan ugrálhat a leggyakrabban látogatott könyvtárak között. A még kevesebb gépelés érdekében olyan álnevek is rendelkezésre állnak, mint a j vagy jc. További információ: <https://github.com/wting/autojump>.

- Ugrás a megadott mintát tartalmazó könyvtárba:

`j {{pattern}}`

- Ugrás az aktuális könyvtár olyan alkönyvtárába (gyermekkönyvtárába), amely tartalmazza az adott mintát:

`jc {{pattern}}`

- Az adott mintát tartalmazó könyvtár megnyitása az operációs rendszer fájlkezelőjében:

`jo {{pattern}}`

- Nem létező könyvtárak eltávolítása az autojump adatbázisból:

`j --purge`

- Az autojump adatbázis bejegyzéseinek megjelenítése:

`j -s`
