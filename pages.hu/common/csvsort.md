# csvsort

> CSV fájlok rendezése. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- CSV fájl rendezése a 9. oszlop szerint:

`csvsort -c {{9}} {{data.csv}}`

- A CSV-fájl rendezése a "név" oszlop szerint csökkenő sorrendben:

`csvsort -r -c {{name}} {{data.csv}}`

- Rendezzen egy CSV-fájlt a 2. oszlop, majd a 4. oszlop szerint:

`csvsort -c {{2,4}} {{data.csv}}`

- CSV-fájl rendezése az adattípusok következtetése nélkül:

`csvsort --no-inference -c {{columns}} {{data.csv}}`
