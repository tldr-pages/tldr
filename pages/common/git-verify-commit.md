# git verify-commit

> Check for GPG verification of commits.
> If no commits are verified, nothing will be printed, regardless of options specified.
> More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit {{commit_hash}} {{optional_commit_hash(s')}}`

- Check commits for a GPG signature and show details of each commit:

`git verify-commit {{commit_hash}} {{optional_commit_hash(s')}} --verbose`

- Check commits for a GPG signature and print raw details:

`git verify-commit {{commit_hash}} {{optional_commit_hash(s')}} --raw`
