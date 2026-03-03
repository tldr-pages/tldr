# cmus-remote

> Control `cmus`.
> See also: `playerctl`.
> More information: <https://manned.org/cmus-remote>.

- [Q]uery player status information:

`cmus-remote -Q`

- Toggle playback:

`cmus-remote {{[-u|--pause]}}`

- Skip to the next song:

`cmus-remote {{[-n|--next]}}`

- Skip back to the previous song:

`cmus-remote {{[-r|--prev]}}`

- Execute a `cmus` command:

`cmus-remote {{[-C|--raw]}} "{{set repeat?}}"`
