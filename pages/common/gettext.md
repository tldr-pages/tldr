# gettext

> Takes a string and tries to return the translated version based on your current language and app settings.
> By default, gettext looks for translations here: "<LOCALEDIR>/<LANG>/LC_MESSAGES/<domain>.mo".
> For example, gettext would look for a Spanish translation file called asd.mo in "locale/es/LC_MESSAGES/asd.mo".
> If no translation exists when gettext is invoked, it returns in English.
> See also: `msgfmt`.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/gettext-Invocation.html>.

- Get the translation of a string, or output a default string if no translation exists:

`LANGUAGE={{locale}} gettext {{msgid}} {{default_value}}`

- Use context to disambiguate where you want the string origin to be located (e.g. Open "File" as a menu item, or linguistically as in "file away the burr"?):

`gettext {{[-c|--context]}} {{context}}`

- Specify the domain (e.g., package, program, module) you want gettext to look inside for the translation:

`gettext {{[-d|--domain]}} {{textdomain}}`

- Display help:

`gettext {{[-h|--help]}}`
