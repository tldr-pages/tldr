# git obliterate

> Ștergeți anumite fișiere și ștergeți istoricul acestora dintr-un depozit Git.
> Parte din `git-extras`.
> Mai multe informaţii: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>

- Ștergeți existența unor fișiere specifice:

`git obliterate {{file_1 file_2 ...}}`

- Ștergeți existența unor fișiere specifice între 2 angajări:

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash_1}}..{{commit_hash_2}}`
