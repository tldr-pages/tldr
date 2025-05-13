# watchman trigger

> Set up a command to run when matching files change in a watched directory.
> More information: <https://facebook.github.io/watchman/>.

- Add a trigger for any matching file change:

`watchman -- trigger {{path/to/watched_directory}} {{trigger_name}} {{file_pattern}} -- {{command}} {{arguments}}`

- Add a trigger for multiple file patterns:

`watchman -- trigger {{path/to/watched_directory}} {{trigger_name}} {{pattern1}} {{pattern2}} -- {{command}} {{arguments}}`
