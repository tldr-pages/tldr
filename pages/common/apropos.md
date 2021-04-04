# apropos

> Search in manpages, for example to find a new command.

- Search for keyword:

`apropos {{regular_expression}}`

- Search without restricting output to terminal width:

`apropos -l {{regular_expression}}`

- Search for pages that only contain all of the expressions given (AND search):

`apropos {{regular_expression_1}} -a {{regular_expression_2}} -a {{regular_expression_3}}`
