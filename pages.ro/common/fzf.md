# fzf

> Finder fuzzy linie de comandă.
> Similar cu `sk`.
> Mai multe informaţii: <https://github.com/junegunn/fzf>

- Porniți fzf pe toate fișierele din directorul specificat:

`find {{path/to/directory}} -type f | fzf`

- Porniți fzf pentru procesele care rulează:

`ps aux | fzf`

- Selectați mai multe fișiere cu `Shift + Tab` și scrieți într-un fișier:

`find {{path/to/directory}} -type f | fzf --multi > {{filename}}`

- Porniți fzf cu o interogare specificată:

`fzf --query "{{query}}"`

- Începeți fzf pe intrările care încep cu miez și se termină fie cu du-te, rb, fie py:

`fzf --query "^core go$ | rb$ | py$"`

- Începeți fzf pe intrările care nu se potrivesc cu pyc și se potrivesc exact Travis:

`fzf --query "!pyc 'travis"`
