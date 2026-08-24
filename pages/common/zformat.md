# zformat

> Format strings in Zsh.
> This builtin is part of the `zsh/zutil` module.
> See also: `zstyle`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- Load the zformat module:

`zmodload zsh/zutil`

- Format a string by replacing `%c` with a value and store the result in a variable:

`zformat -f {{variable}} "{{Hello %c}}" {{c:world}}`

- Format with right-padding (left-align) to a minimum width:

`zformat -f {{variable}} "{{%10c}}" {{c:hello}}`

- Format with left-padding (right-align) using negative width:

`zformat -f {{variable}} "{{%-10c}}" {{c:hello}}`

- Use ternary expression for conditional text (if value is 3, outputs "yes", otherwise "no"):

`zformat -f {{variable}} "{{The answer is '%3(c.yes.no)'.}}" {{c:3}}`

- Format with left-padding (right-align) using negative minimum width:

`zformat -f {{variable}} "name: %-15n value: %-10v" {{n:value1}} {{v:value2}}`

- Align strings (left:right pairs separated by colon):

`zformat -a {{array}} {{:}} {{left1:right1}} {{left2:right2}}`
