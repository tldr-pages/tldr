# rlwrap

> Add line editing, persistent history and prompt completion to an REPL command.
> More information: <https://github.com/hanslub42/rlwrap>.

- Run an REPL command with line editing, persistent history and prompt completion:

`rlwrap {{command}}`

- Use all words seen on input and output for prompt completion:

`rlwrap --remember {{command}}`

- Better prompt completion if prompts contain ANSI colour codes:

`rlwrap --ansi-colour-aware {{command}}`

- Enable filename completion (case sensitive):

`rlwrap --complete-filenames {{command}}`

- Add coloured prompts - one of *black*, *red*, *green*, *yellow*, *blue*, *cyan*, *purple (=magenta)* or *white*, or an ANSI-conformant `colour_spec`. An uppercase colour name (Yellow or YELLOW) gives a bold prompt:

`rlwrap --prompt-colour {{colour}} {{command}}`
