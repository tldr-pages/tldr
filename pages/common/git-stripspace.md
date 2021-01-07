# git stripspace

> Read text (e.g. commit messages, notes, tags, and branch descriptions) from the standard input and clean it into the manner used by Git.
> More information: <https://git-scm.com/docs/git-stripspace>.

- Trim whitespace from a file:

`cat {{path/to/file}} | git stripspace`

- Trim whitespace and Git comments from a file:

`cat {{path/to/file}} | git stripspace --strip-comments`

- Convert all lines in a file into Git comments:

`git stripspace --comment-lines < {{path/to/file}}`
