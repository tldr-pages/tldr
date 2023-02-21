# expr

> Evaluate expressions and manipulate strings.
> More information: <https://www.gnu.org/software/coreutils/expr>.

- Get the length of a specific string:

`expr length "{{string}}"`

- Get the substring of a string with a specific length:

`expr substr "{{string}}" {{from}} {{length}}`

- Match a specific substring against an anchored pattern:

`expr match "{{string}}" '{{pattern}}'`

- Get the first char position from a specific set in a string:

`expr index "{{string}}" "{{chars}}"`

- Calculate a specific mathematic expression:

`expr {{expression1}} {{+|-|*|/|%}} {{expression2}}`

- Get the first expression if its value is non-zero and not null otherwise get the second one:

`expr {{expression1}} \| {{expression2}}`

- Get the first expression if both expressions are non-zero and not null otherwise get zero:

`expr {{expression1}} \& {{expression2}}`
