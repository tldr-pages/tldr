# alias

> Creates an alias for a word when used
> as the first word of a command

- creating a generic alias

`alias {{word}}="{{command}}"`

- remove an aliased command

`unalias {{word}}`

- full list of aliased words

`alias -p`

- turning rm an interative command

`alias {{rm}}="{{rm -i}}"`

- overriding la as ls -a

`alias {{la}}="{{ls -a}}"`
