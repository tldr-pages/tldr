# gpgconf

> Modify .gnupg home directories.
> More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

- List all components:

`gpgconf --list-components`

- List the directories used by gpgconf:

`gpgconf --list-dirs`

- List all options of a component:

`gpgconf --list-options {{component}}`

- List programs and test whether they are runnable:

`gpgconf --check-programs`

- Reload a component:

`gpgconf --reload {{component}}`
