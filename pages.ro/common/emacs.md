# emacs

> Editor extensibil, personalizabil, auto-documentare, afișare în timp real.
> A se vedea, de asemenea, `emacsclient'.
> Mai multe informaţii: <https://www.gnu.org/software/emacs>

- Porniți Emacs și deschideți un fișier:

`emacs {{path/to/file}}`

- Deschideți un fișier la un număr de linie specificat:

`emacs +{{line_number}} {{path/to/file}}`

- Porniți Emacs în modul consolă (fără o fereastră X):

`emacs --no-window-system`

- Porniți un server Emacs în fundal (accesibil prin `emacsclient`):

`emacs --daemon`

- Opriți un server Emacs care rulează și toate instanțele sale, solicitând confirmarea pe fișierele nesalvate:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Salvați un fișier în Emacs:

`Ctrl + X, Ctrl + S`

- Renunţă la Emacs:

`Ctrl + X, Ctrl + C`
