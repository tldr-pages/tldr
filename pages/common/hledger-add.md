# hledger add

> Record new transactions with interactive prompting in the console.
> More information: <https://hledger.org/hledger.html#add>.

- Record new transactions, saving to the default journal file:

`hledger add`

- Add transactions to `2024.journal`, but also load `2023.journal` for completions:

`hledger add --file {{path/to/2024.journal}} --file {{path/to/2023.journal}}`

- Provide answers for the first four prompts:

`hledger add {{today}} '{{best buy}}' {{expenses:supplies}} '{{$20}}'`

- Show `add`'s options and documentation with `$PAGER`:

`hledger add --help`

- Show `add`'s documentation with `info` or `man` if available:

`hledger help add`
