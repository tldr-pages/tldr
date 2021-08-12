# git commit

> Comite fișiere în depozit.
> Mai multe informaţii: <https://git-scm.com/docs/git-commit>

- Comite fișiere pe etape în depozit cu un mesaj:

`git commit -m "{{message}}"`

- Comite fișiere pe etape cu un mesaj citit dintr-un fișier:

`git commit --file {{path/to/commit_message_file}}`

- Etapa automată toate fișierele modificate și comite cu un mesaj:

`git commit -a -m "{{message}}"`

- Commiterea fișierelor pe etape și [S] le puteți ajusta cu tasta GPG definită în `~/.gitconfig`:

`git commit -S -m "{{message}}"`

- Actualizați ultima angajare adăugând modificările în etape în prezent, schimbând hash-ul angajării:

`git commit --amend`

- Comite numai fișiere specifice (deja în etape):

`git commit {{path/to/file1}} {{path/to/file2}}`

- Creați o comitere, chiar dacă nu există fișiere pe etape:

`git commit -m "{{message}}" --allow-empty`
