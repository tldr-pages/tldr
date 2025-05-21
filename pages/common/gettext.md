# gettext

> Takes a string and tries to return the translated version based on your current language and app settings.
> If no translation exists, it returns in English.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/gettext-Invocation.html>.

- Get the translation of a string, or output a default string if no translation exists:

`LANGUAGE={{locale}} gettext {{msgid}} {{default_value}}`

- Use context to disambiguate where you want the string origin to be located (e.g. Open "File" as a menu item, or linguistically as in "file away the burr"?):

`gettext {{[-c|--context]}} {{context}}`

- Specify the domain (e.g., package, program, module) you want gettext to look inside for the translation:

`gettext {{[-d|--domain]}} {{textdomain}}`

- Display help:

`gettext {{[-h|--help]}}`
