# webstorm

> The JetBrains JavaScript IDE.
> More information: <https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>.

- Open the current directory in WebStorm:

`webstorm`

- Open a specific directory in WebStorm:

`webstorm {{path/to/directory}}`

- Open specific files in the LightEdit mode﻿:

`webstorm -e {{path/to/file1 path/to/file2 ...}}`

- Open and wait until done editing a specific file in the LightEdit mode:

`webstorm --wait -e {{path/to/file}}`

- Open a file with the cursor at the specific line:

`webstorm --line {{line_number}} {{path/to/file}}`

- Open and compare files (supports up to 3 files):

`webstorm diff {{path/to/file1}} {{path/to/file2}}`

- Open and perform a three-way merge:

`webstorm merge {{path/to/left_file}} {{path/to/right_file}} {{path/to/target_file}}`
