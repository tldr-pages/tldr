# unzip

> Extract files/directories from Zip archives.
> See also: `zip`.
> More information: <https://manned.org/unzip>.

- Extract all files/directories from a specific archive into the current directory:

`unzip {{path/to/archive}}.zip`

- Extract files/directories from an archive to a specific directory:

`unzip {{path/to/archive}}.zip -d {{path/to/output}}`

- Extract files/directories from an archive to `stdout` alongside the extracted file names:

`unzip -c {{path/to/archive}}.zip`

- Extract an archive created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames:

`unzip -O {{gbk}} {{path/to/archive}}.zip`

- List the contents of a specific archive without extracting them:

`unzip -l {{path/to/archive}}.zip`

- Extract specific files from an archive into the current directory, discarding any directory paths:

`unzip -j {{path/to/archive}}.zip {{path/to/file1_in_archive path/to/file2_in_archive ...}}`
