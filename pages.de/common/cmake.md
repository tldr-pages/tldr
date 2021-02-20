# cmake

> Plattformübergreifes Build-Automatisierungs-System, das Vorlagen für native Build-Systeme erzeugt.
> Mehr Informationen: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Erzeugt eine Build-Vorlage im aktuellen Verzeichnis mit `CMakeLists.txt` eines Projektordners:

`cmake {{pfad/zu/projektordner}}`

- Erzeugt eine Build-Vorlage mit der Build-Art auf `Release` gesetzt:

`cmake {{pfad/zu/projektordner}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Benutze eine generierte Vorlage in einem bestimmten Verzeichnis um Artifakte zu erzeugen:

`cmake --build {{pfad/zu/build_verzeichnis}}`

- Installiere die Build-Artifakte in `/usr/local/` und enferne Debugsymbole:

`cmake --install {{pfad/zu/build_verzeichnis}} --strip`

- Installiere die Build-Artifakte mit einem eigenen Präfix für Pfade:

`cmake --install {{pfad/zu/build_verzeichnis}} --strip --prefix {{pfad/zu/verzeichnis}}`

- Führe ein eigenes Build-Ziel aus:

`cmake --build {{pfad/zu/build_verzeichnis}} --target {{zielname}}`
