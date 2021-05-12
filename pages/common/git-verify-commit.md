# git verify-commit

> Check for GPG verification of commits.
> If GPG verification isn't present, nothing will be returned, even if extra options are chosen.
> More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit {{commit_hash}} {{commit_hash}}`

- Check commits for a GPG signature and show details of each commit:

`git verify-commit {{commit_hash}} --verbose`

- Check commits for a GPG signature and print raw details:

`git verify-commit {{commit_hash}} --raw`
