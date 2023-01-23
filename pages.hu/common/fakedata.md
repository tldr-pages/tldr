# fakedata

> Hamis adatok generálása számos generátor segítségével. További információ: <https://github.com/lucapette/fakedata>.

- Az összes érvényes generátor felsorolása:

`fakedata --generators`

- Adatok generálása egy vagy több generátor segítségével:

`fakedata {{generator1}} {{generator2}}`

- Adatok generálása egy adott kimeneti formátummal:

`fakedata --format {{csv|tab|sql}} {{generator}}`

- Adott számú adatelem generálása (alapértelmezett érték 10):

`fakedata --limit {{n}} {{generator}}`

- Egyéni kimeneti sablon használatával generál adatokat (a generátorok nevének első betűjét nagybetűvel kell írni):

`echo "{{\{\{Generator\}\}}}" | fakedata`
