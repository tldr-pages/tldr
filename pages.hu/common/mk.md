# mk

> Task runner az Mkfile-ban leírt célprogramokhoz. Leginkább a forráskódból származó futtatható program fordításának vezérlésére használják. További információ: <http://doc.cat-v.org/plan_9/4th_edition/papers/mk>.

- Meghívja az Mkfile-ban megadott első célpontot (általában az "all" nevű):

`mk`

- Egy adott célpont meghívása:

`mk {{target}}`

- Egy adott célpont hívása, egyszerre 4 feladat párhuzamos végrehajtása:

`NPROC=4 mk {{target}}`

- Egy célpont mkingjének kikényszerítése, még akkor is, ha a forrásfájlok változatlanok:

`mk -w{{target}} {{target}}`

- Feltételezzük, hogy minden célpont elavult. Így frissítse a `target` és az összes függőségét:

`mk -a {{target}}`

- Hiba esetén folytassa a lehető legmesszebbre:

`mk -k`
