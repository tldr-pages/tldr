# git check-ref-format

> Check if a given refname is acceptable, and exit with a non-zero status if it is not.
> More information: <https://git-scm.com/docs/git-check-ref-format>.

- Check the format of the specified refname:

`git check-ref-format {{refs/head/refname}}`

- Print the name of the last branch checked out:

`git check-ref-format --branch @{-1}`

- Normalize a refname:

`git check-ref-format --normalize {{refs/head/refname}}`
