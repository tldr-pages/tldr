# emacsclient

> Öffnet Dateien in einem bestehenden Emacs Server.
> Weitere Informationen: <https://www.emacswiki.org/emacs/EmacsClient>.

- Öffnen einer Datei (direkt in der GUI wenn möglich):

`emacsclient {{Datei-Name}}`

- Öffnen einer Datei innerhalb der Konsole (ohne X-Fenster):

`emacsclient -nw {{Datei-Name}}`

- Öffnen einer Datei in Emacs mit direktem Zurückkehren in die Konsole:

`emacsclient -n {{Datei-Name}}`

- Öffnen einer Datei in einem neuen Emacs Fenster:

`emacsclient -c {{Datei-Name}}`

- Ausführen eines Kommandos in einem neuen Emacs Fenster:

`emacsclient -c -e '({{Kommando}})'`
