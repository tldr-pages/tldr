# file

> Bestimmen des Dateityps.
> Siehe auch: `stat`.
> Weitere Informationen: <https://manned.org/file>.

- Gib eine Beschreibung des Typs der angegebenen Datei zurück. Funktioniert bei Dateien ohne Dateiendung:

`file {{pfad/zu/datei}}`

- Zeige den Dateipfad nich an:

`file {{[-b|--brief]}} {{pfad/zu/datei}}`

- Bestimme die Dateityp(en) in einer gezippten Datei:

`file {{[-z|--uncompress]}} {{pfad/zu/datei.zip}}`

- Lasse zu, dass die Datei mit speziellen oder Gerätedateien arbeitet:

`file {{[-s|--special-files]}} {{pfad/zu/datei}}`

- Höre nicht bei der ersten Dateityp-Übereinstimmung auf; mache bis zum Ende der Datei weiter:

`file {{[-k|--keep-going]}} {{pfad/zu/datei}}`

- Bestimme den MIME-Codierungstyp einer Datei:

`file {{[-i|--mime]}} {{pfad/zu/datei}}`
