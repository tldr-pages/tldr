# lolcat

> Put a rainbow in everything you `cat` to the console.
> More information: <https://manned.org/lolcat>.

- Print a file to the console in rainbow colors:

`lolcat {{path/to/file}}`

- Print the result of a text-producing command in rainbow colors:

`{{fortune}} | lolcat`

- Use a seed to generate consistent colors (default: `0` as in random):

`lolcat {{[-S|--seed]}} {{number}} {{path/to/file}}`

- Control rainbow frequency (default: `0.1`):

`lolcat {{[-F|--frequency]}} {{number}} {{path/to/file}}`

- Control rainbow smoothing (default: `3`):

`lolcat {{[-p|--spread]}} {{number}} {{path/to/file}}`

- Print a file to the console with animated rainbow colors:

`lolcat {{[-a|--animate]}} {{path/to/file}}`

- Print a file to the console with 24-bit (truecolor) rainbow colors:

`lolcat {{[-t|--truecolor]}} {{path/to/file}}`
