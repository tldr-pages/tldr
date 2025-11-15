# euse

> Enable, disable, and obtain information about Gentoo USE flags.
> More information: <https://wiki.gentoo.org/wiki/Euse>.

- List active global USE flags:

`euse {{[-a|--active]}} {{[-g|--global]}}`

- List active local USE flags:

`euse {{[-a|--active]}} {{[-l|--local]}}`

- Enable a global USE flag:

`sudo euse {{[-E|--enable]}} {{use_flag}}`

- Disable a global USE flag (put a '-' sign in front of the USE flag):

`sudo euse {{[-D|--disable]}} {{use_flag}}`

- Remove a global USE flag:

`sudo euse {{[-P|--prune]}} {{use_flag}}`
