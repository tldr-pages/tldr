# gitui

> A lightweight keyboard-only TUI for Git.
> See also: `tig`, `git-gui`.
> More information: <https://github.com/gitui-org/gitui>.

- Start `gitui` for the repository in the current directory:

`gitui`

- Specify the filename of the color theme loaded from the config directory (defaults to `theme.ron`):

`gitui {{[-t|--theme]}} {{theme2.ron}}`

- Store logging output into a specific file:

`gitui --logfile {{path/to/file}}`

- Inspect a specific file inside the repository in the current directory:

`gitui {{[-f|--file]}} {{path/to/file}}`

- Use notify-based file system watcher instead of tick-based update:

`gitui --watcher`

- Generate a bug report:

`gitui --bugreport`

- Use a specific Git directory:

`gitui {{[-d|--directory]}} {{path/to/directory}}`

- Use a specific working directory:

`gitui {{[-w|--workdir]}} {{path/to/directory}}`
