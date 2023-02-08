# ostree

> Version control for binary files similar to git but optimized for operating system root filesystems.
> OSTree is the foundation for immutable image-based operating systems such as Fedora Silverblue, Fedora IoT or Fedora CoreOS.
> More information: <https://ostreedev.github.io/ostree>.

- Initialize a repository of the files in `$PWD` with metadata in `$PWD/{{path/to/repo}}`:

`ostree init --repo {{path/to/repo}}`

- Create a commit (snapshot) of the files:

`ostree commit --repo {{path/to/repo}} --branch {{branch_name}}`

- Show files in commit:

`ostree ls --repo {{path/to/repo}} {{commit_id}}`

- Show metadata of commit:

`ostree show --repo {{path/to/repo}} {{commit_id}}`

- Show list of commits:

`ostree log --repo {{path/to/repo}} {{branch_name}}`

- Show repo summary:

`ostree summary --repo {{path/to/repo}} --view`

- Show available refs (branches):

`ostree refs --repo {{path/to/repo}}`
