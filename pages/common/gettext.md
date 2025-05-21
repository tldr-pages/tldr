# gettext

> Get string translations.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/gettext-Invocation.html>.

- Get the translation of a string or output a default string if it doesn't exist:

`LANGUAGE={{locale}} gettext {{msgid}} {{default_value}}`

- Use context to disambiguate:

`gettext {{[-c|--context]}} {{context}}`

- Specify domain (e.g., package, program, module):

`gettext {{[-d|--domain]}} {{textdomain}}`

- Display help:

`gettext {{[-h|--help]}}`
