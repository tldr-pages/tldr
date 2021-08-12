# java

> Lansator de aplicații Java.
> Mai multe informaţii: <https://java.com>

- Executa un fisier java `.class` care contine o metoda principala folosind doar numele clasei:

`java {{classname}}`

- Executa un program `.jar`:

`java -jar {{filename.jar}}`

- Executa un program `.jar` cu depanare care asteapta sa se conecteze la portul 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- Afișează versiunile JDK, JRE și HotSpot:

`java -version`

- Afișează informațiile de utilizare pentru comanda java:

`java -help`
