# javap

> Egy vagy több osztályfájl szétszerelése és listázása. További információ: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/javap.html>.

- A `.class` fájl szétszerelése és listázása:

`javap {{path/to/file.class}}`

- Több `.class` fájl szétszerelése és listázása:

`javap {{path/to/file1.class path/to/file2.class ...}}`

- Egy beépített osztályfájl szétszerelése és listázása:

`javap java.{{package}}.{{class}}`

- Súgó megjelenítése:

`javap -help`

- Verzió megjelenítése:

`javap -version`
