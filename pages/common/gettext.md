# gettext

> Translates a string using stored translations in a compiled `.mo` file.
> If no translation is found, the original string is returned.
> You MUST specify `--domain` to point at your file path containing the translated text, even if your file is named `messages.mo`.
> If `--domain` isn't specified, no translation will be returned.
> Example: ES invocation `LANG=es_ES.UTF-8 gettext --domain=messages "Hello"` returns `Hola`, if defined in `/usr/share/locale/es/LC_MESSAGES/messages.mo`.
> See also: `msgfmt`, `msgunfmt`.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/gettext-Invocation.html>.

- Get the translation of a string as specified in the domain file (falls back to given `msgid` if no translation exists):

`LANGUAGE={{locale}} gettext {{[-d|--domain]}} {{domain}} {{msgid}}`

- Display help:

`gettext {{[-h|--help]}}`
