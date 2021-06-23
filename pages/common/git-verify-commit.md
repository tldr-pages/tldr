# git verify-commit

> Check for GPG verification of commits.
> If no commits are verified, nothing will be printed, regardless of options specified.
> More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}}`

- Check commits for a GPG signature and show details of each commit:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --verbose`

- Check commits for a GPG signature and print the raw details:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw`
