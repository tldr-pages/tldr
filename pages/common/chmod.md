# chmod

> Change the access permissions of a file or directory.

- Give the [u]ser who owns a file the right to e[x]ecute it:

`chmod u+x {{file}}`

- Give the user rights to [r]ead and [w]rite to a file/directory:

`chmod u+rw {{file_or_directory}}`

- Remove executable rights from the [g]roup:

`chmod g-x {{file}}`

- Give [a]ll users rights to read and execute:

`chmod a+rx {{file}}`

- Give [o]thers (not in the file owner's group) the same rights as the group:

`chmod o=g {{file}}`

- Change permissions recursively giving [g]roup and [o]thers the abililty to [w]rite:

`chmod -R g+w,o+w {{directory}}`
