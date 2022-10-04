# git stamp

> Stamp the last commit message, with the possibility to reference the issues numbers from your bug tracker or link to its review page.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>.

- Stamp the last commit message referencing it with the issue number from your bug tracker:

`git stamp issue {{FOO-123}}`

- Stamp the last commit message linking it to its review page:

`git stamp review {{https://reviews.example.org/r/4567/}}`

- Stamp the last commit message replacing previous issues with a new one:

`git stamp --replace issue {{BAR-123}}`
