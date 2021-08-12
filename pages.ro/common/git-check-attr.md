# git check-attr

> Pentru fiecare nume de traseu, lista dacă fiecare atribut este nespecificat, setat sau anulat ca gitatribut pe acel nume al traseului.
> Mai multe informaţii: <https://git-scm.com/docs/git-check-attr>

- Verificați valorile tuturor atributelor dintr-un fișier:

`git check-attr --all {{path/to/file}}`

- Verificați valoarea unui atribut specific dintr-un fișier:

`git check-attr {{attribute}} {{path/to/file}}`

- Verificați valoarea unui atribut specific pe fișiere:

`git check-attr --all {{path/to/file1}} {{path/to/file2}}`

- Verificați valoarea unui atribut specific pe unul sau mai multe fișiere:

`git check-attr {{attribute}} {{path/to/file1}} {{path/to/file2}}`
