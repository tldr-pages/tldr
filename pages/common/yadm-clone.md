# yadm-clone

> This command works just like git clone.
> In addition you can pass extra flags to configure your repo.
> If you have a bootstrap file in your repo. You will be prompted to execute it.
> More information: <https://yadm.io/docs/common_commands>.

- Clone your repo:

`yadm clone {{remote_repository_location}}`

- Clone your repo then execute the bootstrap file:

`yadm clone {{remote_repo}} --bootstrap`

- Clone an existing repository and after cloning, do not execute the bootstrap file:

`yadm clone {{remote_repo}} --no-bootstrap`

- Change the worktree that `yadm` will use during cloning:

`yadm clone {{remote_repo}} --w {{worktree_file}}`

- Change the branch that yadm gets files from:

`yadm clone {{remote_repo}} -b {{branch}}`

- Override an existing repository local branch:

`yadm clone {{remote_repo}} -f`
