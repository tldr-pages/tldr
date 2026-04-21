# zstyle

> Format strings in Zsh.
> This builtin is part of the `zsh/zutil` module.
> See also: `zstyle`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- List all defined styles:

`zstyle`

- List styles as ready-to-paste `zstyle` commands:

`zstyle -L`

- Define a style for a pattern:

`zstyle {{pattern}} {{style}} {{value}} ...`

- Delete styles (all, or for a specific pattern/style):

`zstyle -d {{pattern}}`

- Retrieve a style value as a string into a variable:

`zstyle -s {{context}} {{style}} {{name}}`

- Retrieve a style value as a boolean into a variable:

`zstyle -b {{context}} {{style}} {{name}}`

- Retrieve a style value as an array:

`zstyle -a {{context}} {{style}} {{name}}`
