# btm

> A `top` alternatívája. Célja, hogy könnyű, platformokon átívelő és grafikusabb legyen, mint a `top`. További információ: <https://github.com/ClementTsang/bottom>.

- Megjeleníti az alapértelmezett elrendezést (CPU, memória, hőmérséklet, lemez, hálózat és folyamatok):

`btm`

- Az alapmód engedélyezése, a grafikonok eltávolítása és az adatok tömörítése (hasonlóan a `top`):

`btm --basic`

- Nagy pontok használata a kis pontok helyett a diagramokban:

`btm --dot_marker`

- Az akkumulátor töltöttségi és egészségi állapotának megjelenítése:

`btm --battery`

- Frissítés 250 milliszekundumonként, és az utolsó 30 másodperc megjelenítése a grafikonokon:

`btm --rate 250 --default_time_value 30000`
