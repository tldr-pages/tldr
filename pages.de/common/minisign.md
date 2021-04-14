# minisign

> Ein denkbar einfaches Werkzeug um Dateien zu signieren und Signaturen zu verifizieren.
> Mehr Informationen: <https://jedisct1.github.io/minisign/>.

- Ein neues Schlüsselpaar im Standardpfad generieren:

`minisign -G`

- Eine Datei signieren:

`minisign -Sm {{/pfad/zu/datei}}`

- Eine Datei signieren und dabei einen vertrauenswürdigen (signierten) und einen nicht vertrauenswürdigen Kommentar in der Signatur anfügen:

`minisign -Sm {{/pfad/zu/datei}} -c "{{Dieser Kommentar ist nicht vertrauenswürdig.}}" -t "{{Dieser Kommentar ist vertrauenswürdig.}}"`

- Eine Datei und die vertrauenswürdigen Kommentare in ihrer Signatur gegen die angegebene Datei mit dem öffentlichen Schlüssel verifizieren:

`minisign -Vm {{/pfad/zu/datei}} -p {{/pfad/zu/oeffentlicher_schluessel.pub}}`
