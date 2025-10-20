# msgattrib

> Filter and manipulate message attributes in `.po` translation files.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/msgattrib-Invocation.html>.

- Keep only translated messages:

`msgattrib --translated {{input.po}} > {{translated.po}}`

- Keep only untranslated messages:

`msgattrib --untranslated {{input.po}} > {{untranslated.po}}`

- Remove fuzzy messages:

`msgattrib --no-fuzzy {{input.po}} > {{clean.po}}`

- Keep only fuzzy messages:

`msgattrib --only-fuzzy {{input.po}} > {{fuzzy.po}}`

- Mark all messages as fuzzy:

`msgattrib --set-fuzzy {{input.po}} > {{fuzzy.po}}`

- Clear fuzzy marks:

`msgattrib --clear-fuzzy {{input.po}} > {{clean.po}}`

- Sort output by file location:

`msgattrib {{[-F|--sort-by-file]}} {{input.po}} > {{sorted.po}}`

- Display help:

`msgattrib {{[-h|--help]}}`
