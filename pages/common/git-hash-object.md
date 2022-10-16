# git hash-object

> Computes the unique hash key of content and optionally creates an object with specified type.
> More information: <https://git-scm.com/docs/git-hash-object>.

- Compute the ID that would be used to store it in git database:

`git hash-object {{path/to/file}}`

- Compute the object ID and store it in the Git database:

`git hash-object -w {{path/to/file}}`

- Compute the ID and specify the type of object:

`git hash-object -t {{blob|commit|tag|tree}} {{path/to/file}}`

- Compute the ID from stdin:

`cat {{path/to/file}} | git hash-object --stdin`
