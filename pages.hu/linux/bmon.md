# bmon

> A sávszélesség figyelése és a hálózattal kapcsolatos statisztikák rögzítése. További információ: <https://github.com/tgraf/bmon>.

- Az összes interfész listájának megjelenítése:

`bmon -a`

- Az adatátviteli sebességek megjelenítése bit/másodpercben:

`bmon -b`

- Házirend beállítása annak meghatározására, hogy melyik hálózati interfész(ek) jelenjen(ek) meg:

`bmon -p {{interface_1,interface_2,interface_3}}`

- Állítsa be azt az intervallumot (másodpercben), amelyben a számlálónkénti sebesség kiszámításra kerül:

`bmon -R {{2.0}}`
