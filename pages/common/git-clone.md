# git clone

> Clone an existing repository.
> More information: <https://git-scm.com/docs/git-clone>.

- Clone an existing repository into a new directory (the default directory is the repository name):

`git clone {{remote_repository_location}} {{path/to/directory}}`

- Clone an existing repository and its submodules:

`git clone --recursive {{remote_repository_location}}`

- Clone only the `.git` directory of an existing repository:

`git clone --no-checkout {{remote_repository_location}}`

- Clone a local repository:

`git clone --local {{path/to/local/repository}}`

- Clone quietly:

`git clone --quiet {{remote_repository_location}}`

- Clone an existing repository only fetching the 10 most recent commits on the default branch (useful to save time):

`git clone --depth {{10}} {{remote_repository_location}}`

- Clone an existing repository only fetching a specific branch:

`git clone --branch {{name}} --single-branch {{remote_repository_location}}`

- Clone an existing repository using a specific SSH command:

`git clone --config core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{remote_repository_location}}`
