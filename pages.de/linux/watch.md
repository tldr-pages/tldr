# watch

> Führe einen Befehl wiederholt aus und überwache die Ausgabe im Vollbildmodus.
> Weitere Informationen: <https://manned.org/watch>.

- Überwache die Dateien im aktuellen Verzeichnis:

`watch {{ls}}`

- Überwache verfügbaren Festplatten-Speicherplatz und hebe die Änderungen hervor:

`watch -d {{df}}`

- Überwache "node"-Prozesse und aktualisiere alle 3 Sekunden:

`watch -n {{3}} "{{ps aux | grep node}}"`
