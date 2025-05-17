# watchman

> A service that watches files, and triggers actions when changes occur.
> More information: <https://facebook.github.io/watchman/docs/cli-options>.

- Infer the root directory of the project containing the specified directory, and watch its files and sub-folders for changes:

`watchman watch-project {{path/to/directory}}`

- Add a trigger to run a command when files with a specified filename pattern in a watched directory change:

`watchman -- trigger {{path/to/watched_directory}} {{trigger_name}} '{{pattern}}' -- {{command}}`

- List all watched directories:

`watchman watch-list`

- Delete a watch on a directory and its associated triggers:

`watchman watch-del {{path/to/watched_directory}}`

- Delete all watched directories and triggers:

`watchman watch-del-all`

- List all triggers on a watched directory:

`watchman trigger-list {{path/to/watched_directory}}`

- Delete a trigger from a watched directory:

`watchman trigger-del {{path/to/watched_directory}} {{trigger_name}}`

- Temporarily stop `watchman`, until the next time you call a `watchman` command:

`watchman shutdown-server`
