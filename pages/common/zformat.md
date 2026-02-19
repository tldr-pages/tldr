# zformat

> Format strings in Zsh.
> See also: `zstyle`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Format a string into a variable:

`zformat -f {{var}} "{{string with %s placeholders}}" {{arg1}} {{arg2}}`

- Format with left-justification:

`zformat -f {{var}} "{{%10s}}" {{text}}`

- Format with right-justification:

`zformat -f {{var}} "{{% -10s}}" {{text}}`

- Format with zero-padding:

`zformat -f {{var}} "{{%05d}}" {{number}}`

- Format multiple arguments:

`zformat -f {{var}} "{{name: %s, age: %d}}" {{John}} {{30}}`

- Use colon prefix for compact formatting:

`zformat -f {{var}} : "{{%s:%s}}" {{prefix}} {{value}}`

- Format with specified width:

`zformat -f {{var}} "{{%20.20s}}" {{text}}`
