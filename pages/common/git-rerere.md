# git rerere

> Reuse fixes for merge conflicts.
> More information: <https://git-scm.com/docs/git-rerere>.

- Enable rerere globally:

`git config --global rerere.enabled true`

- Forget a file's recorded resolution:

`git rerere forget {{path/to/file}}`

- Check the status of recorded resolutions:

`git rerere status`
