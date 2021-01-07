# git checkout-index

> Copy files from the index to the working tree.
> More information: <https://git-scm.com/docs/git-checkout-index>.

- Restore any files deleted since last commit:

`git checkout-index --all`

- Restore any files deleted or changed since last commit:

`git checkout-index --all --force`

- Restore any files changed since last commit (ignoring deleted files):

`git checkout-index --all --force --no-create`

- Create an export of the tree at the last commit in the specified directory (the trailing slash is important):

`git checkout-index --all --force --prefix={{git-index-export/}}`
