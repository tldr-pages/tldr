# tarsnap

> Manipulate remote Tarsnap encrypted backups.
> Note: you don't need to specify the key file and the cache directory if you configure them on `/usr/local/etc/tarsnap.conf` and/or `~/.tarsnaprc`.
> See also: `tarsnap-keygen`.
> More information: <https://www.tarsnap.com/man-tarsnap.1.html>.

- [c]reate a backup archive of one or more files or direcotries, specifying the cryptographic key and the cache directory:

`tarsnap -c --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Display how much data would be uploaded:

`tarsnap -c --dry-run --print-stats --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List stored archives:

`tarsnap --list-archives --keyfile {{path/to/key_file}}`

- [d]elete a specific archive:

`tarsnap -d --keyfile /usr/tarsnap.key --cachedir /usr/tarsnap-cache -f backup-2008-04-24`

- Lis[t] the contents of a specific archive in [v]erbose mode:

`tarsnap -tv --keyfile {{path/to/key_file}} -f {{archive_name}}`

- Restore specific one or more files or directories from an specific archive:

`tarsnap -x --keyfile {{path/to/key_file}} -f {{archive_name}} usr/home/auser usr/home/anotheruser`

- Copy an archive:

`tarsnap -c --keyfile {{path/to/key_file}} -f {{new_archive_name}} @@{{source_archive_name}}`
