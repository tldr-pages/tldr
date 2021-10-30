# aapt

> Android Asset Packaging Tool.
> Kompiliere und verpacke die Resourcen einer Android App.
> Weitere Informationen: <https://elinux.org/Android_aapt>.

- Liste alle Dateien eines APK Archivs auf:

`aapt list {{pfad/zu/app.apk}}`

- Zeige die Metadaten einer App an (Version, Berechtigungen, usw.):

`aapt dump badging {{pfad/zu/app.apk}}`

- Erstelle ein neues APK Archiv mit den Dateien eines bestimmten Verzeichnisses:

`aapt package -F {{pfad/zu/app.apk}} {{pfad/zu/verzeichnis}}`
