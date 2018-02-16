# phar

> Create, update or extract PHP archives (PHAR).

- Add space-separated files or directories to a Phar file:

`phar add -f {{path/to/phar}} {{files_or_directories}}`

- Delete the specified file or directory from a Phar file:

`phar delete -f {{path/to/phar}} -e {{file_or_directory}}`

- Display full usage information and available hashing/compression algorithms:

`phar help`

- Compress or uncompress files and directories in a Phar file:

`phar compress -f {{path/to/phar}} -c {{algorithm}}`

- Get information about a Phar file:

`phar info -f {{path/to/phar}}`

- Display the contents of a Phar file:

`phar list -f {{path/to/phar}}`

- Sign a Phar file with a specific hash:

`phar sign -f {{path/to/phar}} -h {{hash}}`

- Sign a Phar file with an OpenSSL private key

`phar sign -f {{path/to/phar}} -h openssl -y {{path/to/private_key}}`
