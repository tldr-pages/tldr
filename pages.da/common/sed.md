# sed

> Rediger tekst, programmatisk.
> Mere information: <https://manned.org/man/sed.1posix>.

- Erstat den første forekomst af et regulært udtryk (regular expression) i hver linje af en fil, og print resultatet:

`sed 's/{{regular_expression}}/{{erstat}}/' {{filnavn}}`

- Erstat alle forekomster af et regulært udtryk in en fil, og print resultatet:

`sed -r 's/{{regular_expression}}/{{erstat}}/g' {{filnavn}}`

- Erstat alle forekomster af en streng i en fil, og overskriv filen:

`sed -i 's/{{find}}/{{erstat}}/g' {{filnavn}}`

- Erstat forekomster på linjer der matcher mønstret:

`sed '/{{linje_mønster}}/s/{{find}}/{{erstat}}/' {{filnavn}}`

- Fjern linjer der matcher mønstret:

`sed '/{{linje_mønster}}/d' {{filnavn}}`

- Print de første 11 linjer af en fil:

`sed 11q {{filnavn}}`

- Udfør flere find-og-erstat udtryk i en fil:

`sed -e 's/{{find}}/{{erstat}}/' -e 's/{{find}}/{{erstat}}/' {{filnavn}}`

- Erstat separator `/` med en hvilken som helst anden karakter ikke brugt i find- eller erstat-mønstrene, f.eks. `#`:

`sed 's#{{find}}#{{erstat}}#' {{filnavn}}`
