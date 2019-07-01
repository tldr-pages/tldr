# phpcpd

> A copy and paste detector for PHP code.
> More information: <https://github.com/sebastianbergmann/phpcpd>.

- Analyse duplicated code for a specific file or directory:

`phpcpd {{path/to/file_or_directory}}`

- Analyse using fuzzy matching for variable names:

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- Specify a minimum number of identical lines (defaults to 5):

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- Specify a minimum number of identical tokens (defaults to 70):

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- Exclude a directory from analysis (must be relative to the source):

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- Output the results to a PHP-CPD XML file:

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`
