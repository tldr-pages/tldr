# file

> Bestimmen des Dateityps.
> Weitere Informationen: <https://manned.org/file>.

- Gibt eine Beschreibung des Typs der angegebenen Datei zurück. Funktioniert bei Dateien ohne Dateiendung:

`file {{dateiname}}`

- Bestimmt die Dateityp(en) in einer gezippten Datei:

`file {{[-z|--uncompress]}} {{archiv.zip}}`

- Zulassen, dass die Datei mit speziellen oder Gerätedateien arbeitet:

`file {{[-s|--special-files]}} {{dateiname}}`

- Hört nicht bei der ersten Dateityp-Übereinstimmung auf; weitermachen bis zum Ende der Datei:

`file {{[-k|--keep-going]}} {{dateiname}}`

- Bestimmen des MIME-Codierungstyp einer Datei:

`file {{[-i|--mime]}} {{dateiname}}`
