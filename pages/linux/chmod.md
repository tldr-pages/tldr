# chmod

> Change the access permissions of files and directories.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Give the [u]ser who owns a file the right to e[x]ecute it:

`chmod u+x {{path/to/file}}`

- Give the user rights to [r]ead and [w]rite to a file/directory:

`chmod u+rw {{path/to/file_or_directory}}`

- Remove executable rights from the [g]roup:

`chmod g-x {{path/to/file}}`

- Give [a]ll users rights to read and execute:

`chmod a+rx {{path/to/file}}`

- Give [o]thers (not in the file owner's group) the same rights as the group:

`chmod o=g {{path/to/file}}`

- Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite:

`chmod -R g+w,o+w {{path/to/directory}}`

- Recursively give [a]ll users read permissions to files and e[X]ecute permissions to directories:

`chmod -R a+rX {{path/to/directory}}`
