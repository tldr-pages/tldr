# cloc

> Count, and compute differences of, lines of source code and comments.
> More information: <https://github.com/AlDanial/cloc>.

- Count all the lines of code in a directory:

`cloc {{/path/to/directory}}`

- Count all the lines of code in a directory, displaying a progress bar during the counting process:

`cloc --progress=1 {{/path/to/directory}}`

- Compare 2 directory structures and count the differences between them:

`cloc --diff {{/directory/one}} {{/directory/two}}`
