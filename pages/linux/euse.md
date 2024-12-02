# euse

> Enable, disable, and obtain information about Gentoo USE flags.
> More information: <https://wiki.gentoo.org/wiki/Euse>.

- List active global USE flags:

`euse --active --global`

- List active local USE flags:

`euse --active --local`

- Enable a global USE flag:

`sudo euse --enable {{use_flag}}`

- Disable a global USE flag (put a '-' sign in front of the USE flag):

`sudo euse --disable {{use_flag}}`

- Remove a global USE flag:

`sudo euse --prune {{use_flag}}`
