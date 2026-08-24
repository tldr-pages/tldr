# emulate

> Reset shell options to match a certain shell's behavior.
> Also used to ensure a shell function runs with the default configuration.
> More information: <https://github.com/antonio/zsh-config/blob/master/help/emulate>.

- Print current emulation mode:

`emulate`

- Adjust settings of the current shell session to mimic Bash:

`emulate bash`

- Evaluate a [c]ommand within temporary emulation:

`emulate ksh -c "{{echo hi}}"`

- Emulate the default Zsh, [R]esetting options when possible:

`emulate zsh -R`

- Scope emulation to the current function:

`{{my_function}}() { emulate -L {{zsh|sh|ksh|csh}}; {{ls}} }`
