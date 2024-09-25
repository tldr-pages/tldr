# yadm-clone

> This command works just like git clone.
> In addition you can pass extra flags to configure your repo.
> If you have a bootstrap file in your repo. You will be prompted to execute it.

- To clone your repo:

`yadm clone {{remote_repo}}`

- To clone your repo then execute the bootstrap file:

`yadm clone {{remote_repo}} --bootstrap`

- To clone your repo then not execute the bootstrap file:

`yadm clone {{remote_repo}} --no-bootstrap`

- To change the worktree that yadm will use:

`yadm clone {{remote_repo}} --w {{worktree_file}}`

- If you want to change the branch that yadm gets files from:

`yadm clone {{remote_repo}} -b {{branch}}`

- If you want to override an existing repo **local branch**:

`yadm clone {{remote_repo}} -f`
