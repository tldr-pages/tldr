# jj bisect

> Find the first bad revision using binary search.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-bisect>.

- Find the first bad revision in a range by running a test command:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} {{command}}`

- Find the first bad revision using a shell command:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} -- bash -c "{{command}}"`

- Find the first good revision instead of the first bad one:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} --find-good {{command}}`

- Find the first revision where tests start failing:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} -- cargo test`

- Find the first revision where a file was added:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} --find-good -- test -f {{path/to/file}}`
