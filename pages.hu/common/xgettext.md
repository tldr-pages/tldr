# xgettext

> A gettext karakterláncok kivonása a kódfájlokból. További információ: <https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html>.

- A fájl beolvasása és a karakterláncok kimenete a `messages.po` címre:

`xgettext {{path/to/input_file}}`

- Használjon más kimeneti fájlnevet:

`xgettext --output {{path/to/output_file}} {{path/to/input_file}}`

- Új karakterláncok csatolása egy meglévő fájlhoz:

`xgettext --join-existing --output {{path/to/output_file}} {{path/to/input_file}}`

- Ne adjon metaadatokat tartalmazó fejlécet a kimeneti fájlhoz:

`xgettext --omit-header {{path/to/input_file}}`
