# cs java

> Die Befehle `java` und `java-home` laden JVMs herunter und installieren sie. Der Befehl `java` führt sie auch aus.
> Weitere Informationen: <https://get-coursier.io/docs/cli-java>.

- Zeige die Java-Version mit coursier an:

`cs java -version`

- Führe eine bestimmte Java-Version mit benutzerdefinierten Eigenschaften über coursier aus:

`cs java --jvm {{jvm_name}}:{{jvm_version}} -Xmx32m -X{{another_jvm_opt}} -jar {{pfad/zu/jar_name.jar}}`

- Liste alle verfügbaren JVMs im coursier-Standardindex auf:

`cs java --available`

- Liste alle installierten JVMs im System mit ihrem Speicherort auf:

`cs java --installed`

- Setze eine bestimmte JVM als einmaligen Standard für die Shell-Instanz:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --env`

- Mache die Änderungen an den Standard-JVM-Einstellungen rückgängig:

`eval "$(cs java --disable)"`

- Setze eine bestimmte JVM als Standard für das gesamte System:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --setup`
