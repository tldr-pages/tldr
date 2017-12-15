# hg clone

> Create a copy of an existing repository in a new directory.

- Clone a repository to a specified directory:

`hg clone {{remote_repository_source}} {{destination_path}}`

- Clone a repository on a specific branch:

`hg clone --branch {{branch}} {{remote_repository_source}}`

- Clone a repository with a clean working directory:

`hg clone --noupdate {{remote_repository_source}}`

- Clone a repository to a specific revision, tag or branch:

`hg clone --updaterev {{revision}} {{remote_repository_source}}`

- Clone a repository up to a specific revision without any newer history:

`hg clone --rev {{revision}} {{remote_repository_source}}`
