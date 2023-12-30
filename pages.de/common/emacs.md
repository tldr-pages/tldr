# emacs

> Der erweiterbare, veränderbare und selbst-dokumentierende Echtzeit Text Editor.
> Siehe auch `emacsclient`.
> Weitere Informationen: <https://www.gnu.org/software/emacs>.

- Öffne eine Datei in Emacs:

`emacs {{pfad/zu/datei}}`

- Öffne eine Datei in einer bestimmten Zeile:

`emacs +{{zeilennummer}} {{pfad/zu/datei}}`

- Starte Emacs in der Konsole (ohne X-Fenster):

`emacs --no-window-system`

- Starte einen Emacs-Server im Hintergrund (aufrufbar mit `emacsclient`):

`emacs --daemon`

- Beende einen laufenden Emacs-Server und alle Instanzen und frage nach Bestätigung für ungespeicherte Dateien:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Tastenkombination zum Speichern einer Datei:

`<Ctrl> + X, <Ctrl> + S`

- Tastenkombination zum Beenden von Emacs:

`<Ctrl> + X, <Ctrl> + C`
