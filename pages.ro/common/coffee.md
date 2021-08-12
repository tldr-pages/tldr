# coffee

> Execută scripturi CoffeeScript sau le compilează în JavaScript.
> Mai multe informaţii: <https://coffeescript.org#cli>

- Rulează un script:

`coffee {{path/to/file.coffee}}`

- Compilați în JavaScript și salvați într-un fișier cu același nume:

`coffee --compile {{path/to/file.coffee}}`

- Compilați în JavaScript și salvați într-un fișier de ieșire dat:

`coffee --compile {{path/to/file.coffee}} --output {{path/to/file.js}}`

- Rulați REPL interactiv:

`coffee --interactive`

- Urmăriți script-ul pentru modificări și script-ul re-rula:

`coffee --watch {{path/to/file.coffee}}`
