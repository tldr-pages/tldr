# dconf write

> Write a value to a dconf database path.
> More information: <https://developer.gnome.org/dconf>.

- Write a string to a dconf path (note the nested quotes):

`dconf write {{/example/dconf/path}} "'{{Example Value}}'"`

- Write a boolean to a dconf path:

`dconf write {{/example/dconf/path}} {{true|false}}`

- Write an integer to a dconf path:

`dconf write {{/example/dconf/path}} {{16}}`

- Write an array to a dconf path:

`dconf write {{/example/dconf/path}} "[{{'My First Value', 'My Second Value'}}]"`

- Write an empty array to a dconf path:

`dconf write {{/example/dconf/path}} "@as []"`
