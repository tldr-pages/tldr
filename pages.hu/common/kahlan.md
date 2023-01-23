# kahlan

> Egy egység- és viselkedésvezérelt fejlesztési teszt keretrendszer PHP-hez. További információ: <https://kahlan.github.io>.

- A "spec" könyvtárban található összes specifikáció futtatása:

`kahlan`

- Specifikációk futtatása egy adott konfigurációs fájl segítségével:

`kahlan --config={{path/to/configuration_file}}`

- A specifikációk és a kimenet futtatása egy riporter segítségével:

`kahlan --reporter={{dot|bar|json|tap|verbose}}`

- Specifikációk futtatása kódlefedettséggel (a részletesség 0 és 4 között lehet):

`kahlan --coverage={{detail_level}}`
