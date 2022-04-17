# dconf write

> Write key values in dconf databases.
> See also: `dconf`.
> More information: <https://manned.org/dconf>.

- Write a specific key value:

`dconf write {{/path/to/key}} "{{value}}"`

- Write a specific string key value:

`dconf write {{/path/to/key}} "'{{string}}'"`

- Write a specific integer key value:

`dconf write {{/path/to/key}} "{{5}}"`

- Write a specific boolean key value:

`dconf write {{/path/to/key}} "{{true|false}}"`

- Write a specific array key value:

`dconf write {{/path/to/key}} "[{{'first', 'second', ...}}]"`

- Write a specific empty array key value:

`dconf write {{/path/to/key}} "@as []"`
