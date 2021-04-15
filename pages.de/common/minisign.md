# minisign

> Ein denkbar einfaches Werkzeug um Dateien zu signieren und Signaturen zu verifizieren.
> Mehr Informationen: <https://jedisct1.github.io/minisign/>.

- Ein neues Schlüsselpaar im Standardpfad generieren:

`minisign -G`

- Signiere eine Datei:

`minisign -Sm {{pfad/zu/datei}}`

- Signiere eine Datei und füge dabei einen vertrauenswürdigen (signierten) und einen nicht vertrauenswürdigen (unsignierten) Kommentar in der Signatur an:

`minisign -Sm {{pfad/zu/datei}} -c "{{Nicht vertrauenswürdiger Kommentar}}" -t "{{Vertrauenswürdiger Kommentar}}"`

- Verifiziere eine Datei und die vertrauenswürdigen Kommentare in ihrer Signatur gegen die angegebene Datei mit dem öffentlichen Schlüssel:

`minisign -Vm {{pfad/zu/datei}} -p {{pfad/zu/oeffentlicher_schluessel.pub}}`

- Verifiziere eine Datei und die vertrauenswürdigen Kommentare in ihrer Signatur gegen den angegebenen, in Base64 kodierten öffentlichen Schlüssel:

`minisign -Vm {{pfad/zu/datei}} -P "{{oeffentlicher_schluessel_base64}}"`
