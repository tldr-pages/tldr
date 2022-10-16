# sed

> Rediger tekst, programmatisk.
> Mere information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Udskift den første forekomst af et regulært udtryk (regular expression) i hver linje af en fil, og print resultatet:

`sed 's/{{regular_expression}}/{{replace}}/' {{filename}}`

- Udskift alle forekomster af et regulært udtryk in en fil, og print resultatet:

`sed -r 's/{{regular_expression}}/{{replace}}/g' {{filename}}`

- Udskift alle forekomster af en streng i en fil, og overskriv filen:

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- Udskift forekomster på linjer der matcher mønstret:

`sed '/{{line_pattern}}/s/{{find}}/{{replace}}/' {{filename}}`

- Fjern de linjer der matcher mønstret:

`sed '/{{line_pattern}}/d' {{filename}}`

- Print de første 11 linjer af en fil:

`sed 11q {{filename}}`

- Udfør multiple find-og-erstat udtryk til en fil:

`sed -e 's/{{find}}/{{replace}}/' -e 's/{{find}}/{{replace}}/' {{filename}}`
