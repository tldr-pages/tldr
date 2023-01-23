# zek

> Go struktúra generálása XML-ből. További információ: <https://github.com/miku/zek>.

- Go struktúra generálása egy adott XML-ből a `stdin` oldalról, és a kimenet megjelenítése a `stdout` oldalon:

`cat {{path/to/input.xml}} | zek`

- Go struktúra generálása egy adott XML-ből a `stdin` oldalról és a kimenet elküldése egy fájlba:

`curl -s {{https://url/to/xml}} | zek -o {{path/to/output.go}}`

- Egy Go program példájának generálása egy adott XML-ből a `stdin` oldalról és a kimenet elküldése egy fájlba:

`cat {{path/to/input.xml}} | zek -p -o {{path/to/output.go}}`
