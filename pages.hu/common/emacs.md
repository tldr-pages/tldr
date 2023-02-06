# emacs

> A bővíthető, testreszabható, öndokumentáló, valós idejű megjelenítő szerkesztő. Lásd még: `emacsclient`. További információ: <https://www.gnu.org/software/emacs>.

- Indítsa el az Emacsot, és nyisson meg egy fájlt:

`emacs {{path/to/file}}`

- Egy fájl megnyitása egy megadott sorszámnál:

`emacs +{{line_number}} {{path/to/file}}`

- Egy Emacs Lisp fájl futtatása szkriptként:

`emacs --script {{path/to/file.el}}`

- Az Emacs elindítása konzol üzemmódban (X ablak nélkül):

`emacs --no-window-system`

- Emacs-kiszolgáló indítása a háttérben (elérhető a `emacsclient` oldalon keresztül):

`emacs --daemon`

- Egy futó Emacs-kiszolgáló és annak összes példányának leállítása, megerősítést kérve a mentetlen fájlokra:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Fájl mentése az Emacsban:

`Ctrl + X, Ctrl + S`

- Az Emacs kilépése:

`Ctrl + X, Ctrl + C`
