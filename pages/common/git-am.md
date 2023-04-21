# git am

> Apply patch files and create a commit. Useful when receiving commits via email.
> See also `git format-patch`, which can generate patch files.
> More information: <https://git-scm.com/docs/git-am>.

- Apply and commit changes following a local patch file:

`git am {{path/to/file.patch}}`

- Apply and commit changes following a remote patch file:

`curl -L {{https://example.com/file.patch}} | git apply`

- Abort the process of applying a patch file:

`git am --abort`

- Apply as much of a patch file as possible, saving failed hunks to reject files:

`git am --reject {{path/to/file.patch}}`
