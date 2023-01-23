# xml select

> Válasszon az XML-dokumentumok közül az XPATH-ok segítségével. Tipp: használja a `xml elements` címet egy XML-dokumentum XPATH-jának megjelenítéséhez. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Válassza ki az összes "XPATH1" elemet, és írja ki az "XPATH2" alelem értékét:

`xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{path/to/input.xml|URI}}`

- Az "XPATH1" megfeleltetése és az "XPATH2" értékének újsoros szövegként történő kiírása:

`xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{path/to/input.xml|URI}}`

- Számolja meg az "XPATH1" elemeit:

`xml select --template --value-of "count({{XPATH1}})" {{path/to/input.xml|URI}}`

- Egy vagy több XML-dokumentum összes csomópontjának megszámlálása:

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{path/to/input1.xml|URI}} {{path/to/input2.xml|URI}}`

- A `select` alparancs súgójának megjelenítése:

`xml select --help`
