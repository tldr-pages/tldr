# gradle

> A Gradle egy nyílt forráskódú építő automatizálási rendszer. További információ: <https://gradle.org>.

- Fordítson le egy csomagot:

`gradle build`

- Tesztfeladat kizárása:

`gradle build -x {{test}}`

- Futtatás offline módban, hogy a Gradle ne férjen hozzá a hálózathoz az építések során:

`gradle build --offline`

- Törölje a build könyvtárat:

`gradle clean`

- Android csomag (APK) építése kiadási módban:

`gradle assembleRelease`

- A fő feladatok listázása:

`gradle tasks`

- Az összes feladat listázása:

`gradle tasks --all`
