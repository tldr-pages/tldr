# svgo

> SVG Optimizer: un instrument bazat pe Nod.JS pentru optimizarea fişierelor grafice vectoriale scalabile.
> Se aplică o serie de reguli de transformare (plugin-uri), care pot fi comutate individual.
> Mai multe informaţii: <https://github.com/svg/svgo>

- Optimizați un fișier utilizând pluginurile implicite (suprascrie fișierul original):

`svgo {{test.svg}}`

- Optimizați un fișier și salvați rezultatul într-un alt fișier:

`svgo {{test.svg}} -o {{test.min.svg}}`

- Optimizați toate fișierele SVG dintr-un director (suprascrie fișierele originale):

`svgo -f {{path/to/directory/with/svg/files}}`

- Optimizați toate fișierele SVG dintr-un director și salvați fișierele rezultate într-un alt director:

`svgo -f {{path/to/input/directory}} -o {{path/to/output/directory}}`

- Optimizați conținutul SVG trecut de la o altă comandă și salvați rezultatul într-un fișier:

`{{cat test.svg}} | svgo -i - -o {{test.min.svg}}`

- Optimizați un fișier și imprimați rezultatul:

`svgo {{test.svg}} -o -`

- Optimizați un fișier asigurându-vă că un anumit plugin este activat:

`svgo --enable={{plugin_name}}`

- Afișează pluginurile disponibile:

`svgo --show-plugins`
