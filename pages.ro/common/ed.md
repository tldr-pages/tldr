# ed

> Editorul de text original Unix.
> Mai multe informaţii: <https://man.archlinux.org/man/ed.1>

- Începeți editarea unui document gol (care poate fi salvat ca fișier nou în directorul curent):

`ed`

- Start ed, editarea unui document gol, cu `:` ca indicator prompt de comandă:

`ed -p :`

- Începeți editarea unui fișier existent (aceasta arată numărul de octeți al fișierului încărcat):

`ed -p : {{path/to/file}}`

- Comutați imprimarea explicațiilor de eroare. (În mod implicit, explicațiile nu sunt tipărite și numai o `? `apare):

`H`

- Adăugați text la documentul curent. Marcați finalizarea introducând o perioadă de la sine într-o linie nouă:

`a<Enter>{{text_to_insert}}<Enter>.`

- Tipăriți întregul document (`,` este o scurtătură către intervalul `1, $` care acoperă începutul până la sfârșitul documentului):

`,p`

- Scrieți documentul curent într-un fișier nou (numele fișierului poate fi omis dacă `ed` a fost apelat cu un fișier existent):

`w {{filename}}`

- Renunţă:

`q`
