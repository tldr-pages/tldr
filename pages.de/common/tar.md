# tar

> Archivierungstool.
> Häufig kombiniert mit anderen Methoden zur Komprimierung, wie gzip oder bzip2.
> Weitere Informationen: <https://www.gnu.org/software/tar>.

- Erstelle ein Archiv von Dateien:

`tar cf {{pfad/zu/ziel.tar}} {{pfad/zu/datei1 pfad/zu/datei2 ...}}`

- Erstelle ein mit gzip komprimiertes Archiv:

`tar czf {{ziel.tar.gz}} {{pfad/zu/datei1 pfad/zu/datei2 ...}}`

- Erstelle ein mit gzip komprimiertes Archiv mit relativen Pfaden:

`tar czf {{pfad/zu/ziel.tar.gz}} --directory={{pfad/zu/verzeichnis}} .`

- Extrahiere ein (komprimiertes) Archiv in das derzeitige Verzeichnis im ausführlichen Modus:

`tar xvf {{pfad/zu/quelle.tar[.gz|.bz2|.xz]}}`

- Extrahiere ein Archiv in ein Verzeichnis:

`tar xf {{pfad/zu/quelle.tar}} --directory={{pfad/zu/verzeichnis}}`

- Erstelle ein komprimiertes Archiv und benutze den die Dateiendung des Archivs um die Kompressionsmethode zu wählen:

`tar caf {{pfad/zu/ziel.tar.xz}} {{pfad/zu/datei1 pfad/zu/datei2 ...}}`

- Führe die Inhalte eines tar Archivs auf:

`tar tvf {{pfad/zu/quelle.tar}}`

- Extrahiere Dateien die mit einem Muster übereinstimmen:

`tar xf {{pfad/zu/quelle.tar}} --wildcards "{{*.html}}"`
