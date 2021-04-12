# expr

> Evaluate expressions and manipulate strings.
> More information: <https://www.gnu.org/software/coreutils/expr>.

- Get string length:

`expr length {{string}}`

- Evaluate logical or math expression with an operator ('+', '-', '*', '&', '|', etc.). Special symbols should be escaped:

`expr {{first_argument}} {{operator}} {{second_argument}}`

- Get position of the first character in 'string' that matches 'substring':

`echo $(expr index {{string}} {{substring}})`

- Extract part of the string:

`echo $(expr substr {{string}} {{position_to_start}} {{number_of_characters}}`

- Extract part of the string which matches a regular expression:

`echo $(expr {{string}} : '\({{regular_expression}}\)')`
