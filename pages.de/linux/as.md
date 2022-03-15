# as

> Portabler GNU assembler.
> Hauptsächlich beabsichtigt um output von `gcc` für `ld` vorzubereiten.
> Weitere Informationen: <https://manned.org/as>.

- Assemble eine Datei und schreibe den Output in eine in `a.out`.

`as {{datei.s}}`

- Assemble den Output einer gegebenen Datei:

`as {{datei.s}} -o {{out.o}}`

- Generiere den Output schneller indem Leerzeichen und Kommentare nicht verarbeitet werden. (Sollte nur für vertrauenswürdige Compiler benutzt werden):

`as -f {{datei.s}}`

- Inkludiere einen gegebenen Pfad in der Liste von Verzeichnissen für die Suche nach Dateien:

`as -I {{pfad/zum/verzeichnis}} {{datei.s}}`
