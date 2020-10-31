# decaffeinate

> Converti script CoffeScript in JavaScript moderno.
> Maggiori informazioni: <https://decaffeinate-project.org>.

- Converti un file CoffeeScript in JavaScript:

`decaffeinate {{percorso/al/file.coffee}}`

- Converti un file CoffeeScript v2 in JavaScript:

`decaffeinate --use-cs2 {{percorso/al/file.coffee}}`

- Converti `require` e `module.exports` in `import` ed `export`:

`decaffeinate --use-js-modules {{percorso/al/file.coffee}}`

- Converti un file CoffeeScript, permettendo di esportare nomi:

`decaffeinate --loose-js-modules {{percorso/al/file.coffee}}`
