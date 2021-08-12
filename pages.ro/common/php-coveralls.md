# php-coveralls

> Un client PHP pentru Salopete.
> Mai multe informaţii: <https://php-coveralls.github.io/php-coveralls>

- Trimiteți informații de acoperire la Salopete:

`php-coveralls`

- Trimiteți informații de acoperire la Salopete pentru un anumit director:

`php-coveralls --root_dir {{path/to/directory}}`

- Trimiteți informații de acoperire la Salopete cu o configurație specifică:

`php-coveralls --config {{path/to/.coveralls.yml}}`

- Trimiteți informații de acoperire la Salopete cu ieșire verbose:

`php-coveralls --verbose`

- Trimiteți informații de acoperire la Salopete, excluzând fișierele sursă fără declarații executabile:

`php-coveralls --exclude-no-stmt`

- Trimiteți informații de acoperire la Salopete cu un nume specific de mediu:

`php-coveralls --env {{test|dev|prod}}`

- Specificați mai multe fișiere de acoperire Clover XML pentru a încărca:

`php-coveralls --coverage_clover {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- Ieșiți JSON care va fi trimis la salopetă într-un anumit fișier:

`php-coveralls --json_path {{path/to/coveralls-upload.json}}`
