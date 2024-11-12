# eselect news

> An `eselect` module for reading Gentoo news items.
> Note: Portage will print a notice when a repository is synchronized and there are unread news items.
> More information: <https://wiki.gentoo.org/wiki/Eselect#News>.

- List available news items with their numbers (all by default):

`eselect news list {{all|new}}`

- Print the specified news items:

`eselect news read {{number1 number2 ...}}`

- Print all unread news items:

`eselect news read`

- Mark the specified news items as unread:

`eselect news unread {{number1 number2 ...}}`

- Delete all read news items:

`eselect news purge`

- Print the number of available news items (new by default):

`eselect news count {{all|new}}`
