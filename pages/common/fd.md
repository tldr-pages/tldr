# fd

> A simple, fast and user-friendly alternative to find.

- Find files under current dir that match foo:

`fd foo`

- Find files that begin with foo:

`fd '^foo'`

- Find files matching test with a specific extension and under a specific dir:

`fd --extension js test ./src`

- Find files matching config, include ignored and hidden files:

`fd --hidden --no-ignore config`
