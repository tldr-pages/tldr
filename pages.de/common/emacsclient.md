# emacsclient

> Öffnet Dateien in einem laufenden Emacs-Server.
> Siehe auch: `emacs`.
> Weitere Informationen: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Öffne eine Datei in einem laufenden Emacs-Server (mit GUI wenn möglich):

`emacsclient {{pfad/zu/datei}}`

- Öffne eine Datei in der Konsole (ohne X-Fenster):

`emacsclient {{[-nw|--no-window-system]}} {{pfad/zu/datei}}`

- Öffne eine Datei in einem neuen Emacs Fenster:

`emacsclient {{[-c|--create-frame]}} {{pfad/zu/datei}}`

- Führe einen Befehl aus und schreibe das Ergebnis in `stdout`:

`emacsclient {{[-e|--eval]}} '({{befehl}})'`

- Gib einen alternativen Editor an für den Fall, dass kein Emacs-Server läuft:

`emacsclient {{[-a|--alternate-editor]}} {{editor}} {{pfad/zu/datei}}`

- Beende einen laufenden Emacs-Server und alle Instanzen und frage nach Bestätigung für ungespeicherte Dateien:

`emacsclient {{[-e|--eval]}} '(save-buffers-kill-emacs)'`
