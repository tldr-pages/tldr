# java

> Java-Anwendungslauncher.
> Weitere Informationen: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>.

- Führe eine Java-`.class`-Datei aus, die eine Hauptmethode enthält, verwende nur den Klassennamen:

`java {{klassen_name}}`

- Führe ein Java-Programm aus und verwende zusätzliche Drittanbieter- oder benutzerdefinierte Klassen:

`java -classpath {{pfad/zu/klassen1}}:{{pfad/zu/klassen2}}:. {{klassen_name}}`

- Führe ein `.jar`-Programm aus:

`java -jar {{dateiname.jar}}`

- Führe ein `.jar`-Programm aus, wobei Debug auf eine Verbindung auf Port 5005 wartet:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{dateiname.jar}}`

- Zeige JDK-, JRE- und HotSpot-Versionen:

`java -version`

- Zeige Hilfe:

`java -help`
