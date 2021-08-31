# git bug

> A distributed bug tracker that uses git's internal storage, so no files are added in your project.
> As you would do with commits and branches, you can push your bugs to the same git remote you are already using to collaborate with other people.
> More information: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Create a new identity:

`git bug user create`

- Create a new bug:

`git bug add`

- You can push your new entry to a remote:

`git bug push {{remote}}`

- You can pull for updates:

`git bug pull {{remote}}`

- List existing bugs:

`git bug ls`

- Filter and sort bugs using a query:

`git bug ls "{{status}}:{{open}} {{sort}}:{{edit}}"`

- Search for bugs by text content:

`git bug ls "{{searchquery}}" baz`