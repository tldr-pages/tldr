# code

> Cross platform and extensible code editor.
> More information: <https://github.com/microsoft/vscode>.

- Start Visual Studio Code:

`code`

- Open specific files/directories:

`code {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Compare two specific files:

`code --diff {{path/to/file1}} {{path/to/file2}}`

- Open specific files/directories in a new window:

`code --new-window {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Install/uninstall a specific extension:

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- Print installed extensions:

`code --list-extensions`

- Print installed extensions with their versions:

`code --list-extensions --show-versions`

- Start the editor as a superuser (root) while storing user data in a specific directory:

`sudo code --user-data-dir {{path/to/directory}}`
