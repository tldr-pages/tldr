# alias

> Creates an alias for a word when used as the first word of a command.

- Create a generic alias:

`alias {{word}}="{{command}}"`

- Remove an aliased command:

`unalias {{word}}`

- Full list of aliased words:

`alias -p`

- Turn rm an interative command:

`alias {{rm}}="{{rm -i}}"`

- Override la as ls -a:

`alias {{la}}="{{ls -a}}"`
