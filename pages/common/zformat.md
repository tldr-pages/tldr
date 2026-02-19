# zformat

> Format strings in Zsh.
> This builtin is part of the `zsh/zutil` module.
> See also: `zstyle`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- Load the zformat module:

`zmodload zsh/zutil`

- Format a string, replacing `%c` with a value (in this case `c:hello` replaces `%c` with `hello`):

`zformat -f {{var}} "{{%c}}" {{c:hello}}`

- Format with left-padding to a minimum width:

`zformat -f {{var}} "{{%10c}}" {{c:hello}}`

- Format with right-padding (negative width):

`zformat -f {{var}} "{{%-10c}}" {{c:hello}}`

- Format with truncation to maximum width:

`zformat -f {{var}} "{{%c}}" {{c:hello}}`

- Use ternary expression for conditional text (if value is 3, outputs "yes", otherwise "no"):

`zformat -f {{var}} "The answer is '%3(c.yes.no)'." {{c:3}}`

- Format with left-width and right-width (left:padding:width):

`zformat -f {{var}} "name: %-15s value: %10s" {{name:value1}} {{value:value2}}`

- Align strings using the `-a` option (left:right pairs separated by colon):

`zformat -a {{array}} {{:}} {{left1:right1}} {{left2:right2}}`
