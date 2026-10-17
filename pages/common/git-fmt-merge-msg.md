# git fmt-merge-msg

> Produce a merge commit message from the branches fetched into `FETCH_HEAD`.
> Mostly used internally by `git merge` and `git pull`.
> More information: <https://git-scm.com/docs/git-fmt-merge-msg>.

- Generate a merge commit message for the most recently fetched branches:

`git fmt-merge-msg < .git/FETCH_HEAD`

- Generate a merge commit message from a specific file:

`git fmt-merge-msg {{[-F|--file]}} {{path/to/file}}`

- Include the one-line summaries of the commits being merged:

`git fmt-merge-msg --log < .git/FETCH_HEAD`

- Include at most a specific number of commit summaries:

`git fmt-merge-msg --log={{10}} < .git/FETCH_HEAD`

- Start the message with custom text instead of the branch names:

`git fmt-merge-msg {{[-m|--message]}} "{{message}}" --log < .git/FETCH_HEAD`

- Generate the message as if merging into a different branch:

`git fmt-merge-msg --into-name {{branch}} < .git/FETCH_HEAD`
