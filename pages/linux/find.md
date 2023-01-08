# find

> Find files or directories under the given directory tree, recursively.
> See also: `xargs`.
> More information: <https://www.gnu.org/software/findutils/manual/html_mono/find.html>.

- Search files by a specific case sensitive glob pattern/case insensitive glob pattern/case sensitive regular expression/case insensitive regular expression:

`find {{path/to/search_root_directory}} -type {{f}} -{{name|iname|regex|iregex}} '{{*.sh}}'`

- Set a specific regular expression flavour:

`find {{path/to/search_root_directory}} -type {{f}} -regextype {{emacs|posix-awk|posix-basic|posix-egrep|posix-extended}} -{{regex}} '{{\..*\.sh}}'`

- Search files with a specific size in 512-byte blocks/bytes/2-byte words/kibibytes/mebibytes:

`find {{path/to/search_root_directory}} -type {{f}} -size {{5}}{{b|c|w|k|M|...}}'`

- Search specific blocks/characters/directories/named pipes/regular files:

`find {{path/to/search_root_directory}} -type {{b|c|d|p|f|...}}'`

- Search files and directories owned by a specific user or group:

`find {{path/to/search_root_directory}} -{{user|group}} {{value}}'`

- Group specific conditions:

`find {{path/to/search_root_directory}} {{-not -type f}} -{{and|or}} {{-name '*.sh'}}`

- Execute a specific command for found files and directories:

`find {{path/to/search_root_directory}} {{-not -type f}} -execdir {{stat '{}' ';'}}`
