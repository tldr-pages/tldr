# xgettext

> Extrage șiruri gettext din fișierele de cod.
> Mai multe informaţii: <https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html>

- Scanare fișier și ieșire șiruri de caractere la `messages.po`:

`xgettext {{path/to/input_file}}`

- Utilizați un alt nume de fișier de ieșire:

`xgettext --output {{path/to/output_file}} {{path/to/input_file}}`

- Adaugă șiruri noi la un fișier existent:

`xgettext --join-existing --output {{path/to/output_file}} {{path/to/input_file}}`

- Nu adăugați un antet care conține metadate la fișierul de ieșire:

`xgettext --omit-header {{path/to/input_file}}`
