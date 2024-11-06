# yadm-clone

> Works just like `git clone`. In addition you can pass extra flags to configure your repository.
> If there is a bootstrap file in the repository, you will be prompted to execute it.
> See also: `git clone`.
> More information: <https://yadm.io/docs/common_commands>.

- Clone an existing repository:

`yadm clone {{remote_repository_location}}`

- Clone an existing repository, then execute the bootstrap file:

`yadm clone {{remote_repository_location}} --bootstrap`

- Clone an existing repository and after cloning, do not execute the bootstrap file:

`yadm clone {{remote_repository_location}} --no-bootstrap`

- Change the worktree that `yadm` will use during cloning:

`yadm clone {{remote_repository_location}} --w {{worktree_file}}`

- Change the branch that `yadm` gets files from:

`yadm clone {{remote_repository_location}} -b {{branch}}`

- Override an existing repository local branch:

`yadm clone {{remote_repository_location}} -f`
