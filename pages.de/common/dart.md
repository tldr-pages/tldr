# dart

> Das Werkzeug zur Verwaltung von Dart-Projekten.
> Weitere Informationen: <https://dart.dev/tools/dart-tool>.

- Initialisiere ein neues Dart-Projekt in einem Verzeichnis mit demselben Namen:

`dart create {{projekt_name}}`

- Ausführen einer Dart-Datei:

`dart run {{pfad/zur/datei.dart}}`

- Herunterladen der Abhängigkeiten für das aktuelle Projekt:

`dart pub get`

- Ausführen von Unit-Tests für das aktuelle Projekt:

`dart test`

- Aktualisieren veralteter Projektabhängigkeiten, um Null-Sicherheit zu unterstützen:

`dart pub upgrade --null-safety`

- Kompilieren einer Dart-Datei in eine native Binärdatei:

`dart compile exe {{pfad/zur/datei.dart}}`
