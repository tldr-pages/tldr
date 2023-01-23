# phpspec

> Egy viselkedésvezérelt fejlesztési eszköz PHP-hez. További információ: <https://phpspec.net>.

- Egy osztály specifikációjának létrehozása:

`phpspec describe {{class_name}}`

- Futtassa le az összes specifikációt a "spec" könyvtárban:

`phpspec run`

- Egyetlen specifikáció futtatása:

`phpspec run {{path/to/class_specification_file}}`

- Specifikációk futtatása egy adott konfigurációs fájl segítségével:

`phpspec run -c {{path/to/configuration_file}}`

- Specifikációk futtatása egy adott bootstrap fájlt használva:

`phpspec run -b {{path/to/bootstrap_file}}`

- Kódgenerálási kérések kikapcsolása:

`phpspec run --no-code-generation`

- Hamis visszatérési értékek engedélyezése:

`phpspec run --fake`
