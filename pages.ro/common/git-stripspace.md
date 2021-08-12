# git stripspace

> Citiți textul (de exemplu, comiteți mesaje, note, etichete și descrieri ale ramurii) din intrarea standard și curățați-l în modul utilizat de Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-stripspace>

- Îndepărtați spațiul alb dintr-un fișier:

`cat {{path/to/file}} | git stripspace`

- Trim comentariile spațiilor albe și Git dintr-un fișier:

`cat {{path/to/file}} | git stripspace --strip-comments`

- Conversia tuturor liniilor dintr-un fișier în comentarii Git:

`git stripspace --comment-lines < {{path/to/file}}`
