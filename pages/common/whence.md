# whence

> A Zsh builtin to indicate how a command would be interpreted.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html#index-whence>.

- Interpret `command`, with expansion if defined as an `alias` (similar to the `command -v` builtin):

`whence "{{command}}"`

- Display type of `command`, with location if defined as a function or binary (equivalent to the `type` and `command -V` builtins):

`whence -v "{{command}}"`

- Display type of `command`, with content of shell functions instead of location (equivalent to `which` builtin):

`whence -c "{{command}}"`

- Display type of `command`, with content of shell functions and all occurrences on command path (equivalent to the `where` builtin):

`whence -ca "{{command}}"`

- Search only the `$PATH` for `command`, ignoring builtins, aliases, or shell functions (equivalent to the `where` command):

`whence -p "{{command}}"`
