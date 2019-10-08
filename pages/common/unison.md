# unison

> Bidirectional file synchronisation tool.
> More information: <https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>.

- Sync two directories (creates log first time these two directories are synchronised):

`unison root1 root2`

- Automatically accept the (non-conflicting) defaults:

`unison root1 root2 -auto`

- Ignore some files using a pattern:

`unison root1 root2 -ignore {{pattern}}`

- Show documentation:

`unison -doc {{topics}}`
