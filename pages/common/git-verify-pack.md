# git verify-pack

> Verify packed Git archive files.
> More information: <https://git-scm.com/docs/git-verify-pack>.

- Verify a packed Git archive file:

`git verify-pack {{path/to/pack-file}}`

- Verify a packed Git archive file and show verbose details:

`git verify-pack {{[-v|--verbose]}} {{path/to/pack-file}}`

- Verify a packed Git archive file and only display the statistics:

`git verify-pack {{[-s|--stat-only]}} {{path/to/pack-file}}`
