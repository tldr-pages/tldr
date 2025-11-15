# apropos

> Search the manual pages for names and descriptions.
> More information: <https://manned.org/apropos>.

- Search for a keyword using a `regex`:

`apropos {{regex}}`

- Search without restricting the output to the terminal width (long output):

`apropos {{[-l|--long]}} {{regex}}`

- Search for pages that match all the `regex` given:

`apropos {{regex_1}} {{[-a|--and]}} {{regex_2}} {{[-a|--and]}} {{regex_3}}`
