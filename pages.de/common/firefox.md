# firefox

> Ein gratis Open Source Internet Browser.
> Weitere Informationen: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Starte Firefox und öffne eine Website:

`firefox {{https://www.duckduckgo.com}}`

- Öffne ein neues Fenster:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Öffne ein privates (Inkognito) Fenster:

`firefox --private-window`

- Suche nach "wikipedia" mit der Standard-Suchmaschine:

`firefox --search "{{wikipedia}}"`

- Starte Firefox im sicheren Modus (alle Erweiterungen sind deaktiviert):

`firefox --safe-mode`

- Erstelle eine Bildschirmaufnahme einer Website, ohne die GUI zu starten:

`firefox --headless --screenshot {{pfad/zu/ausgabedatei.png}} {{https://beispiel.de/}}`

- Verwende ein bestimmtes Profil um mehrere einzelne Instanzen gleichzeitig laufen zu lassen:

`firefox --profile {{pfad/zu/verzeichnis}} {{https://beispiel.de/}}`

- Lege Firefox als Standard-Browser fest:

`firefox --setDefaultBrowser`
