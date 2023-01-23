# expect

> Szkript végrehajtó, amely kölcsönhatásba lép más, felhasználói bemenetet igénylő programokkal. További információ: <https://manned.org/expect>.

- Várható szkript végrehajtása egy fájlból:

`expect {{path/to/file}}`

- Egy megadott expect szkript végrehajtása:

`expect -c "{{commands}}"`

- Belépés egy interaktív REPL-be (kilépéshez használja a `exit` vagy a Ctrl + D billentyűkombinációt):

`expect -i`
