# aapt

> Android Asset Packaging Tool: compila e pacchetta le risorse di un'app Android.
> Maggiori informazioni: <https://manned.org/aapt>.

- Elenca i file contenuti in un archivio APK:

`aapt list {{percorso/dell/app}}.apk`

- Visualizza i metadati di un'app (versione, permessi, ecc.):

`aapt dump badging {{percorso/dell/app}}.apk`

- Crea un nuovo archivio APK con file dalla directory specificata:

`aapt package -F {{percorso/dell/app}}.apk {{percorso/della/directory}}`
