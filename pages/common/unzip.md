# unzip

> Extract compressed files in a ZIP archive.
> More information: <https://manned.org/unzip>.

- Extract zip file(s) into working directory:

`unzip {{path/to/file.zip ...}}`

- Extract zip files(s) into specified [d]irectory path:

`unzip {{path/to/file.zip ...}} -d {{path/to/target/directory}}`

- [l]ist the contents of a zip file without extracting:

`unzip -l {{path/to/file.zip}}`

- Extract [c]ontents of the file(s) to stdout, including the extracted file names:

`unzip -c {{path/to/file.zip}}`

- [p]ipe content of specified archive member file(s) to stdout:

`unzip -p {{path/to/file.zip}} {{path/to/archive/member/file ...}}`

- Extract a zip file created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames:

`unzip -O {{gbk}} {{file.zip}}`
