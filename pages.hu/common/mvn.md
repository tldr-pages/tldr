# mvn

> Apache Maven. Java-alapú projektek építésére és kezelésére szolgáló eszköz. További információ: <https://maven.apache.org>.

- Egy projekt lefordítása:

`mvn compile`

- A lefordított kód lefordítása és csomagolása a terjeszthető formátumban, például a `jar`:

`mvn package`

- Kompilálás és csomagolás, a unit tesztek kihagyásával:

`mvn package -DskipTests`

- Az elkészített csomag telepítése a helyi maven tárolóba. (Ez meghívja a fordítási és csomagolási parancsokat is):

`mvn install`

- Törölje a build artifactokat a célkönyvtárból:

`mvn clean`

- Végezzen egy tisztítást, majd hívja meg a csomagolási fázist:

`mvn clean package`

- Tisztítsa meg, majd csomagolja a kódot egy adott build-profillal:

`mvn clean -P{{profile}} package`

- Egy osztály futtatása egy main metódussal:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{arg1 arg2}}"`
