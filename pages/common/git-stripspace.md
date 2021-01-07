# git stripspace

> Read text, such as commit messages, notes, tags and branch descriptions, from the standard input and clean it in the manner used by Git.
> More information: <https://git-scm.com/docs/git-stripspace>.

- Trim whitespace from a file:

`cat {{path/to/file}} | git stripspace`

- Trim whitespace and git comments from a file:

`cat {{path/to/file}} | git stripspace --strip-comments`

- Convert all lines in a file into git comments:

`git stripspace --comment-lines < {{path/to/file}}`
