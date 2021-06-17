# git verify-tag

> Check for GPG verification of tags.
> If tag isn't signed with -s when made, you will get an error regardless of signing.
> More information: <https://git-scm.com/docs/git-verify-tag>.

- Check tags for a GPG signature:

`git verify-tag {{tag1 optional_tag2 ...}}`

- Check tags for a GPG signature and show details of each tag:

`git verify-tag {{tag1 optional_tag2 ...}} --verbose`

- Check tags for a GPG signature and print the raw details:

`git verify-tag {{tag1 optional_tag2 ...}} --raw`
