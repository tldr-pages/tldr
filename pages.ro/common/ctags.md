# ctags

> Generează un fișier index (sau tag) de obiecte lingvistice găsite în fișierele sursă pentru multe limbi de programare populare.
> Mai multe informaţii: <https://ctags.io/>

- Generați etichete pentru un singur fișier și le afișați într-un fișier denumit „tag-uri” din directorul curent, suprascriind fișierul dacă există:

`ctags {{path/to/file}}`

- Generați etichete pentru toate fișierele din directorul curent și le afișați într-un anumit fișier, suprascriind fișierul dacă există:

`ctags -f {{filename}} *`

- Generați etichete pentru toate fișierele din directorul curent și toate subdirectoarele:

`ctags --recurse`
