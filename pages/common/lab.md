# lab

> A CLI for Gitlab.

- Create a merge request and specify remote and target branch:

`lab mr create {{remote}} {{target_branch}}`

- The `lab` CLI can call into `hub` commands. Create a PR of the current branch in origin/master:

`lab pull-request`

- Open the repo in a browser:

`lab browse`

- Compare the local branch with the origin branch in a browser:

`lab compare {{username}}/{{local_branch}} {{target_branch}}`
