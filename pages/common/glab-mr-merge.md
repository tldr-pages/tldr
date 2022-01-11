# glab mr merge

> Merge GitLab merge requests.
> More information: <https://glab.readthedocs.io/en/latest/mr/merge.html>.

- Merge the merge request associated with the current branch interactively:

`glab mr merge`

- Merge the specified merge request, interactively:

`glab mr merge {{mr_number}}`

- Merge the merge request, removing the branch on both the local and the remote:

`glab mr merge --remove-source-branch`

- Squash the current merge request into one commit with the message body and merge:

`glab mr merge --squash --message="{{commit_message_body}}"`

- Display help:

`glab mr merge --help`
