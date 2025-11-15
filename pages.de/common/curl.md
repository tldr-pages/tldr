# curl

> Überträgt Daten von oder zu einem Server.
> Unterstützt die meisten Protokolle, inklusive HTTP, FTP und POP3.
> Weitere Informationen: <https://curl.se/docs/manpage.html>.

- Lade den Inhalt einer URL in eine Datei:

`curl {{http://beispiel.de}} {{[-o|--output]}} {{pfad/zu/datei}}`

- Lade eine Datei von einer URL herunter:

`curl {{[-O|--remote-name]}} {{http://beispiel.de/datei}}`

- Lade eine Datei herunter, folge Weiterleitungen und setze vergangene Dateitransfers automatisch fort:

`curl {{[-f|--fail]}} {{[-O|--remote-name]}} {{[-L|--location]}} {{[-C|--continue-at]}} - {{http://beispiel.de/datei}}`

- Sende formular-codierte Daten (POST Anfragen des Typs `application/x-www-form-urlencoded`). Benutze `--data @dateiname` oder `--data @'-'`, um von `stdin` zu lesen:

`curl {{[-d|--data]}} {{'name=karl-dieter'}} {{http://beispiel.de/formular}}`

- Sende eine Anfrage mit einem extra Header mit einer eigenen HTTP-Methode:

`curl {{[-H|--header]}} {{'X-Mein-Header: 123'}} {{[-X|--request]}} {{PUT}} {{http://beispiel.de}}`

- Sende Daten im JSON-Format und lege den geeigneten Inhaltstyp-Header fest:

`curl {{[-d|--data]}} {{'{"name":"karl-dieter"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://beispiel.de/benutzer/1234}}`

- Übergib einen Benutzernamen und frage nach einem Passwort für die Server-Authentifizierung:

`curl {{[-u|--user]}} {{benutzername}} {{http://beispiel.de}}`

- Übergib Client-Zertifikat und -Schlüssel für eine Ressource und überspringe die Zertifikatsüberprüfung:

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://beispiel.de}}`
