# file

> Bestimmen des Dateityps.
> Weitere Informationen: <https://manned.org/file>.

- Gibt eine Beschreibung des Typs der angegebenen Datei zurück. Funktioniert bei Dateien ohne Dateiendung:

`file {{dateiname}}`

- Bestimmt die Dateityp(en) in einer gezippten Datei:

`file -z {{archiv.zip}}`

- Zulassen, dass die Datei mit speziellen oder Gerätedateien arbeitet:

`file -s {{dateiname}}`

- Hört nicht bei der ersten Dateityp-Übereinstimmung auf; weitermachen bis zum Ende der Datei:

`file -k {{dateiname}}`

- Bestimmen des Mime-Codierungstyp einer Datei:

`file -i {{dateiname}}`
