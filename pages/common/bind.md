# bind

> Bash builtin to manage bash hotkeys and variables.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-bind>.

- List all bound commands and their hotkeys:

`bind {{-p|-P}}`

- Query a command for its hotkey:

`bind -q {{command}}`

- Bind a key:

`bind -x '"{{key_sequence}}":{{command}}'`

- List user defined bindings:

`bind -X`

- Display help:

`help bind`
