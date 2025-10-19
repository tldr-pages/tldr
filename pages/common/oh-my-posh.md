# oh-my-posh

> Cross platform prompt engine for any shell.
> More information: <https://ohmyposh.dev/docs>.

- Display current shell name:

`oh-my-posh get shell`

- Initialize oh-my-posh for Bash:

`eval "$(oh-my-posh init bash --config {{path/to/theme}})"`

- Initialize oh-my-posh for Powershell:

`oh-my-posh init pwsh --config {{path/to/theme}} | Invoke-Expression`

- Initialize oh-my-posh for Zsh:

`eval "$(oh-my-posh init zsh --config {{path/to/theme}})"`

- Enable live reloading:

`oh-my-posh enable reload`

- Disable live reloading:

`oh-my-posh disable reload`

- Print debug information for troubleshooting:

`oh-my-posh debug`

- Update oh-my-posh to latest version:

`oh-my-posh upgrade`
