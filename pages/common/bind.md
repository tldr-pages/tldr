# bind

> Bash builtin to manage bash hotkeys and variables.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Shell-Builtin-Commands>.

- List all bound commands:

`bind -l`

- Query what hotkey a bound command has:

`bind -q {{command}}`

- Bind a key:

`bind -x '"{{key_sequence}}":{{command}}'`
