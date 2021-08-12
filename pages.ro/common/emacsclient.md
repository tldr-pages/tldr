# emacsclient

> Deschideți fișierele într-un server Emacs existent.
> A se vedea, de asemenea, `emacs`.
> Mai multe informaţii: <https://www.emacswiki.org/emacs/EmacsClient>

- Deschideți un fișier într-un server Emacs existent (folosind GUI dacă este disponibil):

`emacsclient {{path/to/file}}`

- Deschideți un fișier în modul consolă (fără o fereastră X):

`emacsclient --no-window-system {{path/to/file}}`

- Deschideți un fișier într-o fereastră Emacs nouă:

`emacsclient --create-frame {{path/to/file}}`

- Evaluați o comandă, imprimați ieșirea la stdout, apoi închideți:

`emacsclient --eval '({{command}})'`

- Specificați un editor alternativ în cazul în care nu rulează niciun server Emacs:

`emacsclient --alternate-editor {{editor}} {{path/to/file}}`

- Opriți un server Emacs care rulează și toate instanțele sale, solicitând confirmarea pe fișierele nesalvate:

`emacsclient --eval '(save-buffers-kill-emacs)'`
