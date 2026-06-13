# cloc

> Count lines of code.
> More information: <https://github.com/AlDanial/cloc#options->.

- Count all the lines of code in a directory:

`cloc {{path/to/directory}}`

- Compare 2 directory structures and count the differences between them:

`cloc --diff {{path/to/directory1}} {{path/to/directory2}}`

- Ignore files that are ignored by VCS, such as files specified in `.gitignore`:

`cloc --vcs git {{path/to/directory}}`

- Display the results for each file instead of each language:

`cloc --by-file {{path/to/directory}}`
