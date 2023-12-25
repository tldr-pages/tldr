# curl

> Überträgt Daten von oder zu einem Server.
> Unterstützt die meisten Protokolle, inklusive HTTP, FTP und POP3.
> Weitere Informationen: <https://curl.se/docs/manpage.html>.

- Lade den Inhalt einer URL in eine Datei:

`curl {{http://beispiel.de}} --output {{pfad/zu/datei}}`

- Lade eine Datei von einer URL herunter:

`curl --remote-name {{http://beispiel.de/datei}}`

- Lade eine Datei herunter, folge Weiterleitungen und setze vergangene Dateitransfers automatisch fort:

`curl --fail --remote-name --location --continue-at - {{http://beispiel.de/datei}}`

- Sende formular-codierte Daten (POST Anfragen des Typs `application/x-www-form-urlencoded`). Benutze `--data @dateiname` oder `--data @'-'`, um von STDIN zu lesen:

`curl --data {{'name=karl-dieter'}} {{http://beispiel.de/formular}}`

- Sende eine Anfrage mit einem extra Header mit einer eigenen HTTP-Methode:

`curl --header {{'X-Mein-Header: 123'}} --request {{PUT}} {{http://beispiel.de}}`

- Sende Daten im JSON-Format und lege den geeigneten Inhaltstyp-Header fest:

`curl --data {{'{"name":"karl-dieter"}'}} --header {{'Content-Type: application/json'}} {{http://beispiel.de/benutzer/1234}}`

- Übergib einen Benutzernamen und frage nach einem Passwort für die Server-Authentifizierung:

`curl --user {{benutzername}} {{http://beispiel.de}}`

- Übergib Client-Zertifikat und -Schlüssel für eine Ressource und überspringe die Zertifikatsüberprüfung:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://beispiel.de}}`
