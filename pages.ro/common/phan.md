# phan

> Un instrument de analiză statică pentru PHP.
> Mai multe informaţii: <https://github.com/phan/phan>

- Generează un `.phan/config.php` în directorul curent:

`phan --init`

- Generează un fișier de configurare Phan folosind un anumit nivel (1 fiind cel mai strict la 5 fiind cel mai puțin strict):

`phan --init --init-level {{level}}`

- Analizează directorul curent:

`phan`

- Analizaţi unul sau mai multe directoare:

`phan --directory {{path/to/directory}} --directory {{path/to/another_directory}}`

- Specificați un fișier de configurare (implicit la `.phan/config.php`):

`phan --config-file {{path/to/config.php}}`

- Specificați modul de ieșire:

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- Specificați numărul de procese paralele:

`phan --processes {{number_of_processes}}`
