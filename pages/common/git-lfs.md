# git lfs

> Work with large files in Git repositories.
> More information: <https://git-lfs.github.com>.

- Initialize Git LFS:

`git lfs install`

- Track files that match a glob:

`git lfs track '{{*.bin}}'`

- Change the Git LFS endpoint URL (useful if the LFS server is separate from the Git server):

`git config -f .lfsconfig lfs.url {{lfs_endpoint_url}}`

- List tracked patterns:

`git lfs track`

- List tracked files that have been committed:

`git lfs ls-files`

- Push all Git LFS objects to the remote server (useful if errors are encountered):

`git lfs push --all {{remote_name}} {{branch_name}}`

- Fetch all Git LFS objects:

`git lfs fetch`

- Checkout all Git LFS objects:

`git lfs checkout`
