# gradle

> Gradle este un sistem de automatizare open source.
> Mai multe informaţii: <https://gradle.org>

- Compilarea unui pachet:

`gradle build`

- Excludeți sarcina de testare:

`gradle build -x {{test}}`

- Rulați în modul offline pentru a împiedica Gradle să acceseze rețeaua în timpul compilărilor:

`gradle build --offline`

- Ștergeți directorul de compilare:

`gradle clean`

- Construiți un pachet Android (APK) în modul de lansare:

`gradle assembleRelease`

- Listați principalele sarcini:

`gradle tasks`

- Listează toate sarcinile:

`gradle tasks --all`
