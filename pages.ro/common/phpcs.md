# phpcs

> Tokenize fișiere PHP, JavaScript și CSS pentru a detecta încălcări ale unui set definit de standarde de codificare.
> Mai multe informaţii: <https://github.com/squizlabs/PHP_CodeSniffer>

- Adulmecați directorul specificat pentru probleme (implicite la standardul PEAR):

`phpcs {{path/to/directory}}`

- Afișează o listă de standarde de codificare instalate:

`phpcs -i`

- Specificați un standard de codificare pentru a valida în raport cu:

`phpcs {{path/to/directory}} --standard {{standard}}`

- Specificați extensiile de fișiere separate prin virgulă pentru a include atunci când sniffing:

`phpcs {{path/to/directory}} --extensions {{file_extension(s)}}`

- Specificați formatul raportului de ieșire (de exemplu, „full”, „xml'”, „json”, „rezumat”):

`phpcs {{path/to/directory}} --report {{format}}`

- Setați variabile de configurare pentru a fi utilizate în timpul procesului:

`phpcs {{path/to/directory}} --config-set {{key}} {{value}}`

- O listă separată prin virgulă de fișiere pentru a încărca înainte de procesare:

`phpcs {{path/to/directory}} --bootstrap {{file(s)}}`

- Nu se recurge în subdirectoare:

`phpcs {{path/to/directory}} -l`
