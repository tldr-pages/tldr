# gettext

> Translates a string using stored translations in a compiled `.mo` file.
> If no translation is found, the original string is returned.
> When using a CLI, you MUST specify `--domain`, even if your file is named `messages.mo`. Otherwise, no translations will be loaded.
> Example:
> `LANG=es_ES.UTF-8 gettext --domain=messages "Hello"` returns `Hola`, if defined in `/usr/share/locale/es/LC_MESSAGES/messages.mo`.
> See also: `msgfmt`, `msgunfmt`.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/gettext-Invocation.html>.

- Get the translation of a string (falls back to original if no translation exists):

`LANG={{locale}} gettext {{[-d|--domain]}}={{domain}} {{msgid}}`

- Display help:

`gettext {{[-h|--help]}}`
