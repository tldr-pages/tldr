# java

> Java alkalmazásindító. További információ: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/java.html>.

- Egy fő metódust tartalmazó java `.class` fájl futtatása csak az osztály nevének használatával:

`java {{classname}}`

- Egy java program futtatása és további harmadik féltől származó vagy felhasználó által definiált osztályok használata:

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{classname}}`

- Egy `.jar` program futtatása:

`java -jar {{filename.jar}}`

- Egy `.jar` program végrehajtása debug-várakozással az 5005-ös porton való csatlakozásra várva:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- JDK, JRE és HotSpot verziók megjelenítése:

`java -version`

- A java parancs használati információinak megjelenítése:

`java -help`
