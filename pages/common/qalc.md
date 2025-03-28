# qalc

> Powerful and easy to use command-line calculator.
> See also: `bc`.
> More information: <https://qalculate.github.io/manual/qalc.html>.

- Launch in interactive mode:

`qalc {{[-i|--interactive]}}`

- Launch in terse mode (print the results only):

`qalc {{[-t|--terse]}}`

- Update currency exchange rates:

`qalc {{[-e|--exrates]}}`

- Perform calculations non-interactively:

`qalc {{66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...}}`

- List all supported functions/prefixes/units/variables:

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- Execute commands from a file:

`qalc {{[-f|--file]}} {{path/to/file}}`
