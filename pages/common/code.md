# code

> Cross platform and extensible code editor.
> More information: <https://code.visualstudio.com/docs/configure/command-line>.

- Start Visual Studio Code:

`code`

- Open specific files/directories:

`code {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Compare two specific files:

`code {{[-d|--diff]}} {{path/to/file1}} {{path/to/file2}}`

- Open specific files/directories in a new window:

`code {{[-n|--new-window]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Install/uninstall a specific extension:

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- Display diagnostic and process information about the running code window:

`code {{[-s|--status]}}`

- Print installed extensions with their versions:

`code --list-extensions --show-versions`

- Start the editor as a superuser (root) while storing user data in a specific directory:

`sudo code --user-data-dir {{path/to/directory}}`
