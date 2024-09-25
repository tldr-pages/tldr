# yadm-init

> Initialize a new, empty repository for tracking dotfiles.
> The repository is stored in `$HOME/.local/share/yadm/repo.git`.

- To execute:

`yadm init`

- By default, **$HOME will be used as the work-tree**, but this can be **overridden with the -w** option:

`yadm init -w {{worktree_folder}}`

- Yadm can be forced to overwrite an existing repository by providing the -f option:

`yadm init -f {{local_repo}}`
