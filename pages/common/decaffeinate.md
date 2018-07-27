# decaffeinate

> Move your CoffeeScript source to JavaScript using modern syntax.

- Convert a CoffeeScript file to JavaScript:

`decaffeinate {{filename}}.coffee`

- Convert a CoffeeScript v2 file to JavaScript:

`decaffeinate --use-cs2 {{filename}}.coffee`

- Convert require and module.exports to import and export:

`decaffeinate --use-js-modules {{filename}}.coffee`

- Convert a CoffeeScript, allow named exports:

`decaffeinate --loose-js-modules {{filename}}.coffee`
