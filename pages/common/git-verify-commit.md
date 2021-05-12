# git verify-commit

> Check for GPG verification of commits.
> If GPG verification isn't present, nothing will be returned, even if extra options are chosen.
> More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit {{commit_SHA1}} {{commit_SHA2}}`

- Check commits for a GPG signature and show details of each commit:

`git verify-commit {{commit_SHA}} --verbose`

- Check commits for a GPG signature and print raw details:

`git verify-commit {{commit_SHA}} --raw`
