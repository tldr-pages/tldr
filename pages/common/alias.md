# alias

> Creates an alias for a word when used.
> As the first word of a command.

- Creating a generic alias:

`alias {{word}}="{{command}}"`

- Remove an aliased command:

`unalias {{word}}`

- Full list of aliased words:

`alias -p`

- Turning rm an interative command:

`alias {{rm}}="{{rm -i}}"`

- Overriding la as ls -a:

`alias {{la}}="{{ls -a}}"`
