# decaffeinate

> Move your CoffeeScript source to modern JavaScript.
> More information: <https://www.npmjs.com/package/decaffeinate#common-options>.

- Convert a CoffeeScript file to JavaScript:

`decaffeinate {{path/to/file.coffee}}`

- Convert a CoffeeScript v2 file to JavaScript:

`decaffeinate --use-cs2 {{path/to/file.coffee}}`

- Convert require and `module.exports` to import and export:

`decaffeinate --use-js-modules {{path/to/file.coffee}}`

- Convert a CoffeeScript, allowing named exports:

`decaffeinate --loose-js-modules {{path/to/file.coffee}}`
