# parallel-lint

> Un instrument pentru verificarea sintaxei fișierelor PHP în paralel.
> Mai multe informaţii: <https://github.com/JakubOnderka/PHP-Parallel-Lint>

- Same un anumit director:

`parallel-lint {{path/to/directory}}`

- Lint un director folosind numărul specificat de procese paralele:

`parallel-lint -j {{processes}} {{path/to/directory}}`

- Lint un director, excluzând directorul specificat:

`parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}`

- Lint un director de fișiere utilizând o listă de extensii separate prin virgulă:

`parallel-lint -e {{php,html,phpt}} {{path/to/directory}}`

- Lint un director și de ieșire rezultatele ca JSON:

`parallel-lint --json {{path/to/directory}}`

- Sint un director și arată rezultatele Git vina pentru rânduri care conțin erori:

`parallel-lint --blame {{path/to/directory}}`
