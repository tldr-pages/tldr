# numbat

> A statically-typed scientific calculator with first-class support for physical units.
> See also: `qalc`, `bc`.
> More information: <https://numbat.dev>.

- Start an interactive session:

`numbat`

- Evaluate one or more expressions:

`numbat {{[-e|--expression]}} '{{2 hours + 30 minutes -> seconds}}'`

- Run a Numbat script:

`numbat {{path/to/script.nbt}}`

- Enter an interactive session after running a script or expression:

`numbat {{[-i|--inspect-interactively]}} {{path/to/script.nbt}}`

- Start without loading the prelude of predefined dimensions and units:

`numbat {{[-N|--no-prelude]}}`

- Generate a default configuration file:

`numbat --generate-config`
