# find

> Find files or directories under the given directory tree, recursively.
> See also: `xargs`.
> More information: <https://manned.org/man/freebsd-13.0/find.1>.

- Search files by a specific case sensitive glob pattern/case insensitive glob pattern/case sensitive regular expression/case insensitive regular expression:

`find {{path/to/search_root_directory}} -type {{f}} -{{name|iname|regex|iregex}} '{{*.sh}}'`

- Search files with a specific size in 512-byte blocks/bytes/2-byte words/kibibytes/mebibytes/gibibytes:

`find {{path/to/search_root_directory}} -type {{f}} -size {{5}}{{b|c|w|k|M|G}}'`

- Search specific blocks/characters/directories/named pipes/regular files/symbolic links/socket/door:

`find {{path/to/search_root_directory}} -type {{b|c|d|p|f|l|s|D}}'`

- Search files/directories owned by a specific user/group:

`find {{path/to/search_root_directory}} -{{user|group}} {{value}}'`

- Group specific conditions:

`find {{path/to/search_root_directory}} {{-not -type f}} -{{and|or}} {{-name '*.sh'}}`

- Execute a specific command for found files/directories:

`find {{path/to/search_root_directory}} {{-not -type f}} -execdir {{stat '{}' ';'}}`
