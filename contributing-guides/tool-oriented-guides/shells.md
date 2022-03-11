## Shell page format

If a page describes a shell, when it's possible try to follow this structure:

- Start an interactive shell session:
- Start an interactive shell session without loading startup configs:
- Execute a command:
- Execute a script:
- Check a script for syntax errors:
- _any other examples_
- Print the version:

If you want to include shell builtin sample please place `(builtin)` word at the end of example description such as:

```md
- Define and export an environmental variable that persists across shell restarts (builtin):

`set --universal --export {{variable_name}} {{variable_value}}`
```

Please consult [fish](https://github.com/tldr-pages/tldr/blob/main/pages/common/fish.md) tldr page for a complete example.
