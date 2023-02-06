# gnuplot

> Egy grafikonrajzoló, amely többféle formátumban ad ki grafikonokat. További információ: <http://www.gnuplot.info/>.

- Indítsa el az interaktív grafikonrajzoló héjat:

`gnuplot`

- A megadott grafikondefiníciós fájl grafikonjának kirajzolása:

`gnuplot {{path/to/definition.plt}}`

- A kimeneti formátum beállítása a definíciós fájl betöltése előtti parancs végrehajtásával:

`gnuplot -e "{{set output "path/to/filename.png" size 1024,768}}" {{path/to/definition.plt}}`

- A gnuplot kilépése után is megmarad a grafikonplot előnézeti ablaka:

`gnuplot --persist {{path/to/definition.plt}}`
