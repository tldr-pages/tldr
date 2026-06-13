# cmake

> Plattformübergreifendes Build-Automatisierungs-System, das Vorlagen für native Build-Systeme erzeugt.
> Weitere Informationen: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Erzeuge eine Build-Vorlage im aktuellen Verzeichnis mit `CMakeLists.txt` eines Projektordners:

`cmake {{pfad/zu/projektordner}}`

- Erzeuge eine Build-Vorlage mit der Build-Art `Release`:

`cmake {{pfad/zu/projektordner}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Benutze eine generierte Vorlage, um Artifakte zu erzeugen:

`cmake --build {{pfad/zu/build_verzeichnis}}`

- Installiere die Build-Artifakte in `/usr/local/` und entferne Debugsymbole:

`cmake --install {{pfad/zu/build_verzeichnis}} --strip`

- Installiere die Build-Artifakte mit einem eigenen Präfix für Pfade:

`cmake --install {{pfad/zu/build_verzeichnis}} --strip --prefix {{pfad/zu/verzeichnis}}`

- Führe ein bestimmtes Build-Ziel aus:

`cmake --build {{pfad/zu/build_verzeichnis}} --target {{zielname}}`
