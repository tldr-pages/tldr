# codium

> Cross platform and extensible open-source code editor, without Microsoft telemetry.
> See also: `code` (Visual Studio Code).
> More information: <https://vscodium.com>.

- Start VSCodium:

`codium`

- Open specific files or directories:

`codium {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Compare two specific files:

`codium --diff {{path/to/file1}} {{path/to/file2}}`

- Open specific files or directories in a new window:

`codium --new-window {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Install or uninstall a specific extension:

`codium --install-extension|--uninstall-extension {{publisher.extension}}`

- Print installed extensions with their versions:

`codium --list-extensions --show-versions`

- Display diagnostic and process information about the running window:

`codium --status`
