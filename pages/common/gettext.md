# gettext

> Translates a string using stored translations in a compiled `.mo` file.
> Translations are stored in `/usr/share/locale/locale_name/LC_MESSAGES/` with `domain` being the filename without its extension.
> See also: `msgfmt`, `msgunfmt`.
> More information: <https://www.gnu.org/software/gettext/manual/gettext.html#gettext-Invocation>.

- Get the translation of a string as specified in the domain file (falls back to given `msgid` if no translation exists):

`LANGUAGE={{locale}} gettext {{[-d|--domain]}} {{domain}} "{{msgid}}"`

- Display help:

`gettext {{[-h|--help]}}`

- Display version:

`gettext {{[-V|--version]}}`
