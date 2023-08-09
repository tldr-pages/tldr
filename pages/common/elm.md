# elm

> Compile and run Elm source files.
> More information: <https://elm-lang.org>.

- Initialize an Elm project, generates an elm.json file:

`elm init`

- Start interactive Elm shell:

`elm repl`

- Compile an Elm file, output the result to an `index.html` file:

`elm make {{source}}`

- Compile an Elm file, output the result to a JavaScript file:

`elm make {{source}} --output={{destination}}.js`

- Start local web server that compiles Elm files on page load:

`elm reactor`

- Install Elm package from <https://package.elm-lang.org>:

`elm install {{author}}/{{package}}`
