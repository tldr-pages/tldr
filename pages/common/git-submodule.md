# git submodule

> Inspects, updates and manages submodules.

- Install a repository's specified submodules:

`git submodule update --init --recursive`

- Add a git repository as a submodule:

`git submodule add {{repository_url}}`

- Update every submodule to its latest commit:

`git submodule foreach git pull`
