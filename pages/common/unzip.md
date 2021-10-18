# unzip

> Extract compressed files in a ZIP archive.
> More information: <https://manned.org/unzip>.

- Extract zip file(s) (for multiple files, separate file paths by spaces):

`unzip {{file(s)}}`

- Extract zip files(s) to given path:

`unzip {{compressed_file(s)}} -d {{path/to/put/extracted_file(s)}}`

- List the contents of a zip file without extracting:

`unzip -l {{file.zip}}`

- Extract the contents of the file(s) to stdout alongside the extracted file names:

`unzip -c {{file.zip}}`

- Extract a zip file created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames:

`unzip -O {{gbk}} {{file.zip}}`
