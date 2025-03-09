# xgettext

> Extract translatable strings wrapped in `gettext()` from source files.
> More information: <https://manned.org/man/xgettext>.

- Extract translatable strings to `messages.po`:

`xgettext {{path/to/file.c}}`

- Define the output file:

`xgettext -o {{messages.pot}} {{path/to/file.c}}`
