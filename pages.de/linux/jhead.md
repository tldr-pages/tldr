# jhead

> Manipulation der Zeitstempel und EXIF Daten in Bilddateien.
> Weitere Informationen: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- Zeige alle EXIF Daten eines JPEG Bildes:

`jhead {{pfad/zu/bild.jpg}}`

- Setze die Dateizeit auf die EXIF Zeit (d.h. die Dateizeit wird geändert):

`jhead -ft {{pfad/zu/bild.jpg}}`

- Setze die EXIF Zeit auf die Dateizeit (d.h. die EXIF Zeit wird geändert):

`jhead -dsft {{pfad/zu/bild.jpg}}`

- Benenne alle Dateinamen der JPEG Bilder nach EXIF Datum/Zeit um (Format: Jahr_Monat_Tag-Stunde_Minute_Sekunde.jpg):

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- Rotiere alle Bilder im aktuellen Ordner verlustfrei (Basierend auf dem EXIF Orientierungstag):

`jhead -autorot *.jpg`

- Korrigiere den EXIF Zeitstempel (Format: Stunden:Minuten:Sekunden). Im Beispiel wird jedes Bild eine Stunde in die Vergangenheit geschoben (z.B. Zeitumstellung vergessen):

`jhead -ta-1:00:00 *.jpg`

- Entferne alle Metadaten einschließlich der Vorschaubilder aus der JPEG Datei:

`jhead -purejpg {{pfad/zu/bild.jpg}}`
