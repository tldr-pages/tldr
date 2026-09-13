# git pack-refs

> Pack heads and tags for efficient repository access.
> More information: <https://git-scm.com/docs/git-pack-refs>.

- Pack all tags and refs that are already packed, leaving other refs alone:

`git pack-refs`

- Pack all refs, including branch heads:

`git pack-refs --all`

- Pack all refs, without removing the loose refs afterward:

`git pack-refs --all --no-prune`

- Pack only refs matching a specific glob pattern:

`git pack-refs --include {{glob_pattern}}`

- Pack all refs except those matching a specific glob pattern:

`git pack-refs --all --exclude {{glob_pattern}}`

- Automatically pack refs as needed, based on the current state of the ref database:

`git pack-refs --auto`
