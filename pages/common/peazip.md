# peazip

> Archive creation/extraction tool and file manager.
> Note: most operations open the PeaZip GUI to confirm or set options.
> More information: <https://peazip.github.io/peazip-command-line.html>.

- Open PeaZip with a specific archive or files to work on interactively:

`peazip {{path/to/archive_or_files}}`

- Add files or directories to a new archive, opening the GUI to set its type and options:

`peazip -add2archive {{path/to/file_or_directory}}`

- Add files or directories to a new `.7z` archive without further prompts:

`peazip -add27z {{path/to/file_or_directory}}`

- Add files or directories to a new `.zip` archive without further prompts:

`peazip -add2zip {{path/to/file_or_directory}}`

- Extract an archive in the current directory, applying the "new folder" policy set in the PeaZip app:

`peazip -ext2neutral {{path/to/archive}}`

- Extract an archive to a new folder named after it, if its root contains more than one entry:

`peazip -ext2folder {{path/to/archive}}`

- Extract an archive to the Downloads directory:

`peazip -ext2downloads {{path/to/archive}}`
