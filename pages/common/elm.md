# elm

> Compile and run Elm source files

- Compile an Elm file, output the result to an index.html file:

`elm make {{source}}`

- Compile an Elm file, output the result to a Javascript file:

`elm make {{source}} --output={{destination}}.js`

- Install Elm package from https://package.elm-lang.org

`elm install {{author}}/{{package}}`

- Initialize an Elm project, generates an elm.json file:

`elm init`

- Start interactive Elm shell:

`elm repl`

- Start local server that compiles Elm files on page load:

`elm reactor`
