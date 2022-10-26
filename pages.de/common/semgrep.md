# semgrep

> Durchführung einer *statischen Code-Analyse* (SAST) für einen Quellcode.
> Dient der Aufspürung von Sicherheitsproblemen im Code.
> Semgrep ist ein SAST Tool, welches auf eine sehr hohe Ausführgeschwindigkeit und geringe False Positiverate optimiert wurde.
> Weitere Informationen: <https://semgrep.dev/>.

- Führe semgrep auf ein Verzeichnis aus und verwende dabei automatisch ausgewählte Regeln:

`semgrep --config=auto {{quellcode_verzeichnis}}`

- Führe semgrep auf ein Verzeichnis aus und wähle dabei die Regeln manuell aus:

`semgrep --config p/{{regelsatz_name}} [--config p/{{weiterer_regelsatz_name}} ...] {{quellcode_verzeichnis}}`

- Starte semgrep in einem Docker Container für das aktuelle Verzeichnis:

`docker run --rm -v "${PWD}:/src" returntocorp/semgrep [--config p/{{regelsatz_name}} ...]`
