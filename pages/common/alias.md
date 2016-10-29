# alias

> Creates an alias for a word when used as the first word of a command.
> Note that these operations are not permanent, expiring when the current shell session ends.

- Create a generic alias:

`alias {{word}}="{{command}}"`

- Remove an aliased command:

`unalias {{word}}`

- List all aliased words:

`alias -p`

- Turn rm into an interactive command:

`alias {{rm}}="{{rm -i}}"`

- Create `la` as a shortcut for `ls -a`:

`alias {{la}}="{{ls -a}}"`
