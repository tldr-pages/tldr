# aws lambda

> CLI az AWS lambda számára. További információ: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Futtasson egy függvényt:

`aws lambda invoke --function-name {{name}} {{path/to/response}}.json`

- Futtasson egy függvényt JSON formátumú bemeneti hasznos teherrel:

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response}}.json`

- Függvények listázása:

`aws lambda list-functions`

- Egy függvény konfigurációjának megjelenítése:

`aws lambda get-function-configuration --function-name {{name}}`

- Funkció aliasok listázása:

`aws lambda list-aliases --function-name {{name}}`

- Egy függvény lefoglalt párhuzamossági konfigurációjának megjelenítése:

`aws lambda get-function-concurrency --function-name {{name}}`

- Annak felsorolása, hogy mely AWS-szolgáltatások hívhatják meg a függvényt:

`aws lambda get-policy --function-name {{name}}`
