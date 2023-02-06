# sdk

> Eszköz több szoftverfejlesztői készlet párhuzamos verzióinak kezelésére. Támogatja a Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x és sok más programcsomagot. További információ: <https://sdkman.io/usage>.

- Telepítsen egy SDK verziót:

`sdk install {{sdk_name}} {{sdk_version}}`

- Egy adott SDK-verzió használata az aktuális terminálmunkamenethez:

`sdk use {{sdk_name}} {{sdk_version}}`

- Bármely elérhető SDK stabil verziójának megjelenítése:

`sdk current {{sdk_name}}`

- Az összes telepített SDK stabil verziójának megjelenítése:

`sdk current`

- Az összes elérhető SDK listázása:

`sdk list`

- Egy SDK összes verziójának listázása:

`sdk list {{sdk_name}}`

- SDK frissítése a legújabb stabil verzióra:

`sdk upgrade {{sdk_name}}`

- Egy adott SDK verzió eltávolítása:

`sdk rm {{sdk_name}} {{sdk_version}}`
