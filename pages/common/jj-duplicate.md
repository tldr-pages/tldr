# jj duplicate

> Create new changes with the same content as existing ones.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-duplicate>.

- Duplicate the current revision onto its existing parent:

`jj duplicate`

- Duplicate a specific revision onto its existing parent:

`jj duplicate {{revset}}`

- Duplicate a revision onto a different parent:

`jj duplicate --destination {{dest_revset}} {{revset}}`

- Duplicate a revision and insert it **after** other revision(s):

`jj duplicate --insert-after {{after_revset}} {{revset}}`

- Duplicate a revision and insert it **before** other revision(s):

`jj duplicate --insert-before {{before_revset}} {{revset}}`

- Duplicate onto multiple parents (creates a merge commit):

`jj duplicate --destination {{destination1}} --destination {{destination2}} {{revset}}`

- Duplicate multiple revisions:

`jj duplicate {{revset1 revset2 ...}}`
