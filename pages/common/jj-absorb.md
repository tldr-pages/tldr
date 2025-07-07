# jj absorb

> Split changes in the source revision and move each change to the closest mutable ancestor where the corresponding lines were modified last.
> Changes that have zero or multiple matching regions in ancestral revisions won't be moved.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-absorb>.

- Move all eligible and unambiguous changes from a revision to other revisions automatically:

`jj absorb {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revsets}}`

- Move only changes in given files from a revision to other revisions:

`jj absorb {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revsets}} {{filesets}}`
