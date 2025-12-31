# cbonsai

> A beautifully random bonsai tree generator.
> See also: `cmatrix`, `asciiquarium`, `pipes.sh`.
> More information: <https://gitlab.com/jallbrit/cbonsai>.

- Generate a bonsai in live mode:

`cbonsai {{[-l|--live]}}`

- Generate a bonsai in infinite mode:

`cbonsai {{[-i|--infinite]}}`

- Set the growth factor of the tree (default: 32):

`cbonsai {{[-L|--life]}} {{0..200}}`

- Set the branching factor of the tree (default: 5):

`cbonsai {{[-M|--multiplier]}} {{0..20}}`

- Run in screensaver mode (equivalent to `--live --infinite` but any keypress exits):

`cbonsai {{[-S|--screensaver]}}`

- Append a message to the bonsai:

`cbonsai {{[-m|--message]}} "{{message}}"`

- Display extra information about the bonsai:

`cbonsai {{[-v|--verbose]}}`

- Display help:

`cbonsai {{[-h|--help]}}`
