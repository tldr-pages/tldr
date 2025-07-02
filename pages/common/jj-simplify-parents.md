# jj simplify-parents

> Simplify parent edges for the specified revision(s).
> For example, "A -> B -> C | A -> C" gets simplified to "A -> B -> C".
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-simplify-parents>.

- Simplify parent edges of given revisions:

`jj simplify-parents {{[-r|--revisions]}} {{revsets}}`

- Simplify parent edges of given revisions and trees of their descendants:

`jj simplify-parents {{[-s|--source]}} {{revsets}}`
