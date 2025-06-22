# git stripspace

> Read text (e.g. commit messages, notes, tags, and branch descriptions) from `stdin` and clean it into the manner used by Git.
> More information: <https://git-scm.com/docs/git-stripspace>.

- Trim whitespace from a file:

`git stripspace < {{path/to/file}}`

- Trim whitespace and Git comments from a file:

`git stripspace {{[-s|--strip-comments]}} < {{path/to/file}}`

- Convert all lines in a file into Git comments:

`git stripspace {{[-c|--comment-lines]}} < {{path/to/file}}`
