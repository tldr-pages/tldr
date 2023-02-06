# jar

> Java alkalmazások/könyvtárak csomagolója. További információ: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Az aktuális könyvtárban lévő összes fájl rekurzív archiválása egy .jar fájlba:

`jar cf {{file.jar}} *`

- .jar/.war fájl kicsomagolása az aktuális könyvtárba:

`jar -xvf {{file.jar}}`

- A .jar/.war fájl tartalmának listázása:

`jar tf {{path/to/file.jar}}`

- A .jar/.war fájl tartalmának listázása bőbeszédű kimenettel:

`jar tvf {{path/to/file.jar}}`
