# yacas

> Yet Another Computer Algebra System. További információ: <http://www.yacas.org>.

- Indítson interaktív munkamenetet a `yacas` oldalon:

`yacas`

- A `yacas` munkamenetben egy utasítás végrehajtása:

`{{Integrate(x)Cos(x)}};`

- A `yacas` munkamenetben egy példa megjelenítése:

`{{Example()}};`

- Kilépés a `yacas` munkamenetből:

`{{quit}}`

- Egy vagy több `yacas` szkript végrehajtása (terminál vagy promptok nélkül), majd kilépés:

`yacas -p -c {{path/to/script1}} {{path/to/script2}}`

- Egy utasítás végrehajtása és eredményének kinyomtatása, majd kilépés:

`echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -p -c /dev/stdin`
