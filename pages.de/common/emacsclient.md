# emacsclient

> Öffnet Dateien in einem laufenden Emacs Server.
> Weitere Informationen: <https://www.emacswiki.org/emacs/EmacsClient>.

- Öffne eine Datei (direkt in der GUI wenn möglich):

`emacsclient {{pfad/zu/datei}}`

- Öffne eine Datei in der Konsole (ohne X-Fenster):

`emacsclient -nw {{pfad/zu/datei}}`

- Öffne eine Datei in Emacs mit direktem Zurückkehren in die Konsole:

`emacsclient -n {{pfad/zu/datei}}`

- Öffne eine Datei in einem neuen Emacs Fenster:

`emacsclient -c {{pfad/zu/datei}}`

- Führe einen Befehl in einem neuen Emacs Fenster aus:

`emacsclient -c -e '({{befehl}})'`
