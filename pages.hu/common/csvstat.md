# csvstat

> Leíró statisztikák nyomtatása egy CSV-fájl összes oszlopára. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- Összes oszlop összes statisztikájának megjelenítése:

`csvstat {{data.csv}}`

- A 2. és 4. oszlop összes statisztikájának megjelenítése:

`csvstat -c {{2,4}} {{data.csv}}`

- Összes oszlopok összegének megjelenítése:

`csvstat --sum {{data.csv}}`

- A 3. oszlop maximális értékhosszának megjelenítése:

`csvstat -c {{3}} --len {{data.csv}}`

- A "name" oszlopban az egyedi értékek számának megjelenítése:

`csvstat -c {{name}} --unique {{data.csv}}`
