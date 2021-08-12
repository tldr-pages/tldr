# jar

> Aplicații Java/Biblioteci Packager.
> Mai multe informaţii: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>

- Arhivați recursiv toate fișierele din directorul curent într-un fișier.jar:

`jar cf {{file.jar}} *`

- Dezarhivați fișierul.jar/.war în directorul curent:

`jar -xvf {{file.jar}}`

- Listează un conținut de fișier.jar/.war:

`jar tf {{path/to/file.jar}}`

- Listează un conținut de fișier.jar/.war cu ieșire verbose:

`jar tvf {{path/to/file.jar}}`
