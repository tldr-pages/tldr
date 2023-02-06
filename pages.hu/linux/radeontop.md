# radeontop

> Az AMD GPU-k kihasználtságának megjelenítése. Rendszertől függően root jogosultságokat igényelhet. További információk: <https://github.com/clbr/radeontop>.

- Az alapértelmezett AMD GPU kihasználtságának megjelenítése:

`radeontop`

- Színes kimenet engedélyezése:

`radeontop --color`

- Válasszon ki egy adott GPU-t (a busz száma az első szám a `lspci` kimenetén):

`radeontop --bus {{bus_number}}`

- Adja meg a kijelző frissítési sebességét (a magasabb érték nagyobb GPU-feladatot jelent):

`radeontop --ticks {{samples_per_second}}`
