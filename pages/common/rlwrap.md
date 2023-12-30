# rlwrap

> Add line editing, persistent history and prompt completion to a REPL command.
> More information: <https://github.com/hanslub42/rlwrap>.

- Run a REPL command with line editing, persistent history and prompt completion:

`rlwrap {{command}}`

- Use all words seen on input and output for prompt completion:

`rlwrap --remember {{command}}`

- Better prompt completion if prompts contain ANSI colour codes:

`rlwrap --ansi-colour-aware {{command}}`

- Enable filename completion (case sensitive):

`rlwrap --complete-filenames {{command}}`

- Add coloured prompts, use colour name, or an ASCI-conformant colour specification. Use an uppercase colour name for bold styling:

`rlwrap --prompt-colour={{black|red|green|yellow|blue|cyan|purple|white|colour_spec}} {{command}}`
