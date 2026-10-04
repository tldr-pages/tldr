# kbdrate

> Set the keyboard repeat rate and the delay before a held key starts repeating.
> More information: <https://kbd-project.org/manpages/man8/kbdrate.8.html>.

- Reset the repeat rate and delay to their defaults:

`sudo kbdrate`

- Set the repeat rate in characters per second:

`sudo kbdrate {{[-r|--rate]}} {{15}}`

- Set the delay before repeating in milliseconds:

`sudo kbdrate {{[-d|--delay]}} {{500}}`

- Set both values without printing status messages:

`sudo kbdrate {{[-s|--silent]}} {{[-r|--rate]}} {{15}} {{[-d|--delay]}} {{500}}`

- Display help:

`kbdrate {{[-h|--help]}}`
