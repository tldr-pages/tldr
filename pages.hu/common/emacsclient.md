# emacsclient

> Fájlok megnyitása egy meglévő Emacs-kiszolgálóban. Lásd még: `emacs`. További információ: <https://www.emacswiki.org/emacs/EmacsClient>.

- Fájl megnyitása egy meglévő Emacs-kiszolgálón (GUI használatával, ha van):

`emacsclient {{path/to/file}}`

- Fájl megnyitása konzol üzemmódban (X ablak nélkül):

`emacsclient --no-window-system {{path/to/file}}`

- Fájl megnyitása egy új Emacs ablakban:

`emacsclient --create-frame {{path/to/file}}`

- Egy parancs kiértékelése, a kimenet kinyomtatása a `stdout` címre, majd kilépés:

`emacsclient --eval '({{command}})'`

- Alternatív szerkesztő megadása arra az esetre, ha nem futna Emacs-kiszolgáló:

`emacsclient --alternate-editor {{editor}} {{path/to/file}}`

- Egy futó Emacs-kiszolgáló és annak összes példányának leállítása, megerősítést kérve a mentetlen fájlokra:

`emacsclient --eval '(save-buffers-kill-emacs)'`
