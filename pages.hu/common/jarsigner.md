# jarsigner

> Java archívum (JAR) fájlok aláírása és ellenőrzése. További információ: <https://docs.oracle.com/javase/9/tools/jarsigner.htm>.

- JAR-fájl aláírása:

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- JAR-fájl aláírása egy adott algoritmussal:

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- JAR-fájl aláírásának ellenőrzése:

`jarsigner -verify {{path/to/file.jar}}`
