# elm

> Compilați și executați fișiere sursă Elm.
> Mai multe informaţii: <https://elm-lang.org>

- Inițializarea unui proiect Elm, generează un fișier elm.json:

`elm init`

- Începe coajă Elm interactiv:

`elm repl`

- Compilați un fișier Elm, ieșiți rezultatul într-un fișier `index.html`:

`elm make {{source}}`

- Compilați un fișier Elm, ieșiți rezultatul într-un fișier JavaScript:

`elm make {{source}} --output={{destination}}.js`

- Porniți serverul web local care compilează fișierele Elm pe încărcarea paginii:

`elm reactor`

- Instalați pachetul Elm de la https://package.elm-lang.org:

`elm install {{author}}/{{package}}`
