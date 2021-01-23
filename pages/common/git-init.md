# git init

> Initializes a new local Git repository.
> More information: <https://git-scm.com/docs/git-init>.

- Initialize a new local repository:

`git init`

- Initialize a repository using SHA256 for object hashes (requires Git version 2.29+):

`git init --object-format={{sha256}}`

- Initialize a barebones repository, suitable for use as a remote over ssh:

`git init --bare`
