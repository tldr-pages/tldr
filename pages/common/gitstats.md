# gitstats

> Git repository statistics generator.
> More information: <https://gitstats.readthedocs.io/en/latest/usage.html>.

- Generate statistics for a local repository:

`gitstats {{path/to/git_repo/.git}} {{path/to/output_folder}}`

- View generated statistics in a web browser on Windows (PowerShell)/macOS/Linux:

`{{Invoke-Item|open|xdg-open}} {{path/to/output_folder/index.html}}`

- Display help:

`gitstats {{[-h|--help]}}`
