# phpunit

> PHPUNIT linia de comandă alergător de testare.
> Mai multe informaţii: <https://phpunit.de>

- Rulați teste în directorul curent. Notă: Se așteaptă să aveți un „phpunit.xml”:

`phpunit`

- Executați teste într-un anumit fișier:

`phpunit {{path/to/TestFile.php}}`

- Executați teste adnotate cu grupul dat:

`phpunit --group {{name}}`

- Rulați teste și generați un raport de acoperire în HTML:

`phpunit --coverage-html {{directory}}`
