# phar

> Create, update or extract PHP archives (PHAR).
> More information: <https://manned.org/phar>.

- Add space-separated files or directories to a Phar file:

`phar add -f {{path/to/phar_file}} {{files_or_directories}}`

- Display the contents of a Phar file:

`phar list -f {{path/to/phar_file}}`

- Delete the specified file or directory from a Phar file:

`phar delete -f {{path/to/phar_file}} -e {{file_or_directory}}`

- Compress or uncompress files and directories in a Phar file:

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- Get information about a Phar file:

`phar info -f {{path/to/phar_file}}`

- Sign a Phar file with a specific hash algorithm:

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- Sign a Phar file with an OpenSSL private key:

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`

- Display help and available hashing/compression algorithms:

`phar help`
