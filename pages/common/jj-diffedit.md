# jj diffedit

> Touch up the content changes in a revision with a diff editor.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-diffedit>.

- Edit changes in the current revision with a diff editor:

`jj diffedit`

- Edit changes in a given revision:

`jj diffedit {{[-r|--revision]}} {{revset}}`

- Edit changes comparing a "from" revision to a "to" revision:

`jj diffedit {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}}`

- Edit only specific paths (unmatched paths remain unchanged):

`jj diffedit {{filesets}}`

- Use a specific diff editor:

`jj diffedit --tool {{name}}`

- Preserve content instead of diff when rebasing descendants:

`jj diffedit --restore-descendants`
