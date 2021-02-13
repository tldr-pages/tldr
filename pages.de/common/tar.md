# tar

> Werkzeug zur Archivierung.
> Häufig kombiniert mit einer methode zur Komprimierung, wie gzip oder bzip2.
> Mehr Informationen: <https://www.gnu.org/software/tar>.

- Erstelle ein Archiv von Datein:

`tar cf {{ziel.tar}} {{datei1}} {{datei2}} {{datei3}}`

- Erstelle ein mit gzip komprimiertes Archiv:

`tar czf {{ziel.tar.gz}} {{datei1}} {{datei2}} {{datei3}}`

- Erstelle ein mit gzip komprimiertes Archiv mit relativen Pfaden:

`tar czf {{ziel.tar.gz}} -C {{pfad/zu/verzeichniss/}} .`

- Extrahiere ein (komprimiertes) Archiv in das derzeitige Verzeichniss:

`tar xf {{quelle.tar[.gz|.bz2|.xz]}}`

- Extrahiere ein Archiv in ein Verzeichniss:

`tar xf {{quelle.tar}} -C {{verzeichniss}}`

- Erstelle ein komprimiertes Archiv; benutze den Archiv Suffix um die Kompressions Methode zu wählen:

`tar caf {{ziel.tar.xz}} {{datei1}} {{datei2}} {{datei3}}`

- Führe die Inhalte eines tar Archivs auf:

`tar tvf {{quelle.tar}}`

- Extrahiere Dateien die mit einem Muster übereinstimmen:

`tar xf {{quelle.tar}} --wildcards "{{*.html}}"`

- Extrahiere eine bestimmte Datei ohne die Verzeichniss Struktur beizubehalten:

`tar xf {{quelle.tar}} {{quelle.tar/pfad/zum/extrahieren}} --strip-components={{tiefe_zu_entfernen}}`
