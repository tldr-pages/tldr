# gnomon

> Segédprogram a konzol naplózási utasításainak időbélyegekkel való megjegyzésére és a lassú folyamatok megtalálására. További információ: <https://github.com/paypal/gnomon>.

- A UNIX (vagy DOS) pipek segítségével bármely parancs `stdout` címét átvezetheti a gnomon:

`{{npm test}} | gnomon`

- A folyamat indulása óta eltelt másodpercek számának megjelenítése:

`{{npm test}} | gnomon --type=elapsed-total`

- Abszolút időbélyeg megjelenítése UTC-ben:

`{{npm test}} | gnomon --type=absolute`

- Állítson be egy 0,5 másodperces magas küszöbértéket az eltelt időre; ennek túllépése esetén az időbélyeg élénkpiros színű lesz:

`{{npm test}} | gnomon --high {{0.5}}`

- Állítson be egy közepes küszöbértéket 0,2 másodpercben (az időbélyeg élénksárga színű lesz):

`{{npm test}} | gnomon --medium {{0.2}}`
