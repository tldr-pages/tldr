# phpcpd

> Un detector de copiere și lipire pentru codul PHP.
> Mai multe informaţii: <https://github.com/sebastianbergmann/phpcpd>

- Analizează codul duplicat pentru un anumit fișier sau director:

`phpcpd {{path/to/file_or_directory}}`

- Analizează folosind potrivirea fuzzy pentru numele variabilelor:

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- Specificați un număr minim de linii identice (valori implicite la 5):

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- Specificați un număr minim de token-uri identice (valori implicite la 70):

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- Excludeți un director din analiză (trebuie să fie relativ la sursă):

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- Ieșiți rezultatele într-un fișier XML PHP-CPD:

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`
