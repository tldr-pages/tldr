# phpcbf

> Remediați încălcările detectate de phpcs.
> Mai multe informaţii: <https://github.com/squizlabs/PHP_CodeSniffer>

- Remediați problemele din directorul specificat (implicite la standardul PEAR):

`phpcbf {{path/to/directory}}`

- Afișează o listă de standarde de codificare instalate:

`phpcbf -i`

- Specificați un standard de codificare pentru a valida în raport cu:

`phpcbf {{path/to/directory}} --standard {{standard}}`

- Specificați extensiile de fișiere separate prin virgulă pentru a include atunci când sniffing:

`phpcbf {{path/to/directory}} --extensions {{file_extension(s)}}`

- O listă separată prin virgulă de fișiere pentru a încărca înainte de procesare:

`phpcbf {{path/to/directory}} --bootstrap {{file(s)}}`

- Nu se recurge în subdirectoare:

`phpcbf {{path/to/directory}} -l`
