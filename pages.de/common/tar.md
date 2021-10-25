# tar

> Archivierungs Tool.
> Häufig kombiniert mit anderen Methoden zur Komprimierung, wie gzip oder bzip2.
> Weitere Informationen: <https://www.gnu.org/software/tar>.

- Erstelle ein Archiv von Dateien:

`tar cf {{pfad/zu/ziel.tar}} {{pfad/zu/datei1}} {{pfad/zu/datei2}} {{pfad/zu/datei3}}`

- Erstelle ein mit gzip komprimiertes Archiv:

`tar czf {{ziel.tar.gz}} {{pfad/zu/datei1}} {{pfad/zu/datei2}} {{pfad/zu/datei3}}`

- Erstelle ein mit gzip komprimiertes Archiv mit relativen Pfaden:

`tar czf {{pfad/zu/ziel.tar.gz}} -C {{pfad/zu/verzeichniss/}} .`

- Extrahiere ein (komprimiertes) Archiv in das derzeitige Verzeichniss:

`tar xf {{pfad/zu/quelle.tar[.gz|.bz2|.xz]}}`

- Extrahiere ein Archiv in ein Verzeichniss:

`tar xf {{pfad/zu/quelle.tar}} -C {{verzeichniss}}`

- Erstelle ein komprimiertes Archiv und benutze den Archiv Suffix um die Kompressionsmethode zu wählen:

`tar caf {{ziel.tar.xz}} {{pfad/zu/datei1}} {{pfad/zu/datei2}} {{pfad/zu/datei3}}`

- Führe die Inhalte eines tar Archivs auf:

`tar tvf {{pfad/zu/quelle.tar}}`

- Extrahiere Dateien die mit einem Muster übereinstimmen:

`tar xf {{pfad/zu/quelle.tar}} --wildcards "{{*.html}}"`
