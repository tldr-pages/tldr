# jarsigner

> Semnați și verificați fișierele Java Archive (JAR).
> Mai multe informaţii: <https://docs.oracle.com/javase/9/tools/jarsigner.htm>

- Semneaza un fisier JAR:

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- Semnați un fișier JAR cu un algoritm specific:

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- Verificați semnătura unui fișier JAR:

`jarsigner -verify {{path/to/file.jar}}`
