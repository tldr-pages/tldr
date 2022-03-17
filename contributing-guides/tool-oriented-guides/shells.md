## Shell page format

If the page describes the shell, when it's possible try to follow this structure:

```
- Start the interactive shell session:

`<example>`

- Start the interactive shell session without loading startup configs:

`<example>`

- Execute the command:

`<example>`

- Execute the script:

`<example>`

- Check the script for syntax errors:

`<example>`

# any other examples
```

If you want to include shell builtin sample please place `(builtin)` word at the end of example description such as:

```md
- Define and export the environmental variable that persists across shell restarts (builtin):

`set --universal --export {{variable_name}} {{variable_value}}`
```
