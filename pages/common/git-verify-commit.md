# git verify-commit

> Check for GPG verification of commits.
> If GPG verification isn't present, nothing will be returned, even if extra options are chosen.
> More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit {{commit SHA hash}}`

- Check git commits for a GPG signature and show details of specified commit:

`git verify-commit {{commit SHA hash}} --verbose`

- Check commits for a GPG signature and give RAW details:

`git verify-commit {{commit SHA hash}} --raw`
