# zstyle

> Define and lookup configuration styles in Zsh.
> This builtin is part of the `zsh/zutil` module.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- List all defined styles:

`zstyle`

- List styles as ready-to-paste `zstyle` commands:

`zstyle -L`

- Define a style for a specific pattern:

`zstyle {{pattern}} {{style}} {{value1 value2...}}`

- Delete a style for a specific pattern:

`zstyle -d {{pattern}}`

- Retrieve a style value as a string into a variable:

`zstyle -s {{context}} {{style}} {{variable_name}}`

- Retrieve a style value as a boolean into a variable:

`zstyle -b {{context}} {{style}} {{variable_name}}`
`
- Retrieve a style value as an array:

`zstyle -a {{context}} {{style}} {{variable_name}}`
