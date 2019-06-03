# git clone

> Clone an existing repository.
> More information: <https://git-scm.com/docs/git-clone>.

- Clone an existing repository:

`git clone {{remote_repository_location}}`

- Clone an existing repository and its submodules:

`git clone --recursive {{remote_repository_location}}`

- For cloning from the local machine:

`git clone -l`

- Do it quietly:

`git clone -q`

- Clone an existing repository, and truncate to the specified number of revisions, save your time mostly:

`git clone --depth {{10}} {{remote_repository_location}}`
