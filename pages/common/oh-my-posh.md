# oh-my-posh

> A cross-platform prompt theme engine for any shell.
> Provides consistent and customizable shell prompts across operating systems.
> More Information: https://ohmyposh.dev/docs.

- Display current shell name:

`oh-my-posh get shell`

- Initialize oh-my-posh for Bash:

`eval "$(oh-my-posh init bash --config ~/<theme>.omp.json)"`

- Initialize oh-my-posh for Powershell:

`oh-my-posh init pwsh --config ~/<theme>.omp.json | Invoke-Expression`

- Initialize oh-my-posh for Zsh:

`eval "$(oh-my-posh init zsh --config ~/<theme>.omp.json)"`

- Install Nerd font:

`oh-my-posh font install 3270`

- Enable live reloading:

`oh-my-posh enable reload`

- Disable live reloading:

`oh-my-posh disable reload`

- Preview the changes:

`oh-my-posh print preview`

- Print debug information for troubleshooting:

`oh-my-posh debug`

- Update oh-my-posh to latest version:

`oh-my-posh upgrade`

- Show the version of oh-my-posh:

`oh-my-posh version`
