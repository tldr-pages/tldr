# ant

> Apache Ant.
> Tool zum Bauen und Verwalten von Projekten, die auf Java basieren.
> Weitere Informationen: <https://ant.apache.org>.

- Baue ein Projekt mit der Standard build-Datei `build.xml`:

`ant`

- Baue ein Projekt mit einer anderen build-Datei als `build.xml`:

`ant -f {{buildfile.xml}}`

- Zeige Informationen über mögliche targets für dieses Projekt:

`ant -p`

- Zeige Debugging-Informationen:

`ant -d`

- Führe alle targets aus, die nicht von fehlgeschlagenen targets abhängen:

`ant -k`
