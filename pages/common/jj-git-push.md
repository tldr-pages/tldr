# jj git push

> Push to a Git remote.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-push>.

- Push a bookmark to the given remote (defaults to `git.push` setting):

`jj git push {{[-b|--bookmark]}} {{bookmark}} --remote {{remote}}`

- Push a new bookmark:

`jj git push {{[-b|--bookmark]}} {{bookmark}} {{[-N|--allow-new]}}`

- Push all tracked bookmarks:

`jj git push --tracked`

- Push all bookmarks (including new bookmarks):

`jj git push --all`

- Push all bookmarks pointing to given revisions:

`jj git push {{[-r|--revisions]}} {{revset}}`

- Push changes/commits by creating new bookmarks (Name format is as per `templates.git_push_bookmark` setting, defaults to `"push-" ++ change_id.short()`):

`jj git push {{[-c|--change]}} {{revset}}`

- Push a revision with the given name:

`jj git push --named {{name}}={{revision}}`
