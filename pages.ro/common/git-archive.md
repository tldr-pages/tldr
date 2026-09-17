# git archive

> Creează o arhivă de fișiere dintr-un arbore.
> Mai multe informații: <https://git-scm.com/docs/git-archive>.

- Creează o arhivă `.tar` din conținutul `HEAD`-ului curent și o tipărește la `stdout`:

`git archive {{[-v|--verbose]}} HEAD`

- Folosește formatul Zip și raportează progresul în detaliu:

`git archive {{[-v|--verbose]}} --format zip HEAD`

- Scrie arhiva Zip într-un fișier specific:

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{cale/către/fișier.zip}} HEAD`

- Creează o arhivă `.tar` din conținutul ultimului commit al unei ramuri specifice:

`git archive {{[-o|--output]}} {{cale/către/fișier.tar}} {{nume_ramură}}`

- Folosește conținutul unui director specific:

`git archive {{[-o|--output]}} {{cale/către/fișier.tar}} HEAD:{{cale/către/director}}`

- Adaugă un prefix de cale la fiecare fișier pentru a-l arhiva în interiorul unui director specific:

`git archive {{[-o|--output]}} {{cale/către/fișier.tar}} --prefix {{cale/către/prefix}}/ HEAD`
