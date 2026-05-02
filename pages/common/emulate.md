# emulate

> Reset shell options to match a certain shell's behavior.
> Also used to ensure a shell function runs with the default configuration.
> More information: <https://github.com/antonio/zsh-config/blob/master/help/emulate>.

- Print current emulation mode:

`emulate`

- Adjust settings of the current shell session to mimic bash:

`emulate bash`

- Evaluate some script within a temporary emulation:

`emulate ksh -c "echo hi"`

- Emulate the default zsh, reseting options when possible:

`emulate zsh -R`

- Make option changes by emulate local to a function:

`myfunction() {emulate -L sh; ls}`
