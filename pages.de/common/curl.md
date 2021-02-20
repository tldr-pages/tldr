# curl

> Überträgt Daten von oder zu einem Server.
> Unterstützt die meisten Protokolle, inklusive HTTP, FTP und POP3.
> Mehr Informationen: <https://curl.se>.

- Lade den Inhalt einer URL in eine Datei:

`curl {{http://beispiel.de}} -o {{dateiname}}`

- Lade eine Datei herunter und speichere dan Inhalt in einen Dateinamen, der von der URL vorgegeben wird:

`curl -O {{http://beispiel.de/dateiname}}`

- Lade eine Datei herunter, folge Weiterleitungen und setze vergangene Dateitransfers automatisch fort:

`curl -O -L -C - {{http://beispiel.de/dateiname}}`

- Sende formular-codierte Daten (POST Anfragen des Typs `application/x-www-form-urlencoded`). Benutze `-d @dateiname` oder `-d @'-'`, um von STDIN zu lesen:

`curl -d {{'name=karl-dieter'}} {{http://beispiel.de/formular}}`

- Sende eine Anfrage mit einem extra Header mit einer eigenen HTTP-Methode:

`curl -H {{'X-Mein-Header: 123'}} -X {{PUT}} {{http://beispiel.de}}`

- Sende Daten als JSON-Format und lege den geeigneten Inhaltstyp-Header fest:

`curl -d {{'{"name":"karl-dieter"}'}} -H {{'Content-Type: application/json'}} {{http://beispiel.de/benutzer/1234}}`

- Übergib einen Benutzernamen und Passwort für Server-Authentifizierung:

`curl -u meinbenutzername:meinpasswort {{http://beispiel.de}}`

- Übergib Client-Zertifikat und -Schlüssel für eine Resource und überspringe Zertifikatsüberprüfung:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://beispiel.de}}`
