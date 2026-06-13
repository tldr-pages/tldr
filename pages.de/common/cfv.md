# cfv

> Command-line File Verify, eine Anwendung zum Testen und Erstellen von Prüfsummendateien.
> Weitere Informationen: <https://manned.org/cfv>.

- [T]este Prüfsummendateien im aktuellen Verzeichnis:

`cfv -T`

- [T]este mit ausführlicher Ausgabe [v], be[n]enne fehlerhafte Dateien um, und gib [u]nverifizierte Dateien zurück. Verwende dazu eine bestimmte Prüfsummendatei [f]:

`cfv -Tvnu -f {{pfad/zu/datei}}`

- Erstelle [C] eine Prüfsummendatei unter Verwendung eines bestimmten [t]yps für die ausgewählten Dateien:

`cfv -C -t "{{sfv|sha256|md5|...}}" {{datei1 datei2 ...}}`

- Erstelle [C] separate Prüfsummendateien für jedes [r]ekursiv ausgewählte Verzeichnis:

`cfv -Cr`

- Erstelle [C] eine einzelne `sha256`-Datei [f] für alle [rr]ekursiv ausgewählten Dateien:

`cfv -C -f {{sums.sha256}} -rr`

- Erstelle [C] eine `g[z]ip`-komprimierte `.sfv`-Datei mit ausführlicher Ausgabe [v]. Folge dabei `sym[l]inks` und verwende `pfad/zu/verzeichnis` als Basis[p]fad:

`cfv -Czvl -p {{pfad/zu/verzeichnis}}`
