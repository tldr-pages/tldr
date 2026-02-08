# wget

> Lade Dateien aus dem Internet herunter.
> Unterstützt HTTP, HTTPS und FTP.
> Siehe auch: `wcurl`, `curl`.
> Weitere Informationen: <https://www.gnu.org/software/wget/manual/wget.html>.

- Lade den Inhalt einer URL in eine Datei herunter (in diesem Fall "foo" genannt):

`wget {{https://example.com/foo}}`

- Lade den Inhalt einer URL in eine Datei herunter (in diesem Fall "bar" genannt):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Lade eine einzelne Webseite und alle ihre Ressourcen mit 3-Sekunden-Intervallen zwischen Anfragen herunter (Skripte, Stylesheets, Bilder, etc.):

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/some_page.html}}`

- Lade alle gelisteten Dateien in einem Verzeichnis und seinen Unterverzeichnissen herunter (lädt keine eingebetteten Seitenelemente herunter):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/some_path/}}`

- Begrenze die Download-Geschwindigkeit und die Anzahl der Verbindungsversuche:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/some_path/}}`

- Lade eine Datei von einem HTTP-Server mit Basic Auth herunter (funktioniert auch für FTP):

`wget --user {{benutzername}} --password {{passwort}} {{https://example.com}}`

- Setze einen unvollständigen Download fort:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Lade alle URLs herunter, die in einer Textdatei gespeichert sind, in ein bestimmtes Verzeichnis:

`wget {{[-P|--directory-prefix]}} {{pfad/zu/verzeichnis}} {{[-i|--input-file]}} {{pfad/zu/URLs.txt}}`
