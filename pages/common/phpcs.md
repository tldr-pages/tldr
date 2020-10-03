# phpcs

> Tokenize PHP, JavaScript and CSS files to detect violations of a defined set of coding standards.
> More information: <https://github.com/squizlabs/PHP_CodeSniffer>.

- Sniff the specified directory for issues (defaults to the PEAR standard):

`phpcs {{path/to/directory}}`

- Display a list of installed coding standards:

`phpcs -i`

- Specify a coding standard to validate against:

`phpcs {{path/to/directory}} --standard {{standard}}`

- Specify comma-separated file extensions to include when sniffing:

`phpcs {{path/to/directory}} --extensions {{file_extension(s)}}`

- Specify the format of the output report (e.g. `full`, `xml`, `json`, `summary`):

`phpcs {{path/to/directory}} --report {{format}}`

- Set config variables to be used during the process:

`phpcs {{path/to/directory}} --config-set {{key}} {{value}}`

- A comma-separated list of files to load before processing:

`phpcs {{path/to/directory}} --bootstrap {{file(s)}}`

- Don't recurse into subdirectories:

`phpcs {{path/to/directory}} -l`
