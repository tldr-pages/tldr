# eselect locale

> An `eselect` module for managing the `$LANG` environment variable, which sets the system language.
> More information: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- List available locales:

`eselect locale list`

- Set the `$LANG` environment variable in `/etc/profile.env` by name or index from the `list` command:

`eselect locale set {{name|index}}`

- Display the value of `$LANG` in `/etc/profile.env`:

`eselect locale show`
