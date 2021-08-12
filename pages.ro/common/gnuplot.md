# gnuplot

> Un plotter grafic care emite în mai multe formate.
> Mai multe informaţii: <http://www.gnuplot.info/>

- Porniți carcasa grafic interactiv:

`gnuplot`

- Se trasează graficul pentru fișierul de definiție grafic specificat:

`gnuplot {{path/to/definition.plt}}`

- Setați formatul de ieșire executând o comandă înainte de încărcarea fișierului de definiție:

`gnuplot -e "{{set output "path/to/filename.png" size 1024,768}}" {{path/to/definition.plt}}`

- Persistă fereastra de previzualizare a graficului după ieșirea gnuplot:

`gnuplot --persist {{path/to/definition.plt}}`
