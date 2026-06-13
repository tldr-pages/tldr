# git-lfs-transfer

> Server-side implementation of the Git LFS pure SSH transfer protocol.
> Allows Git LFS to upload and download large files over SSH instead of HTTPS.
> More information: <https://github.com/charmbracelet/git-lfs-transfer#usage>.

- Upload large files tracked by Git LFS to a repository:

`git-lfs-transfer {{path/to/repo.git}} upload`

- Download large files tracked by Git LFS from a repository:

`git-lfs-transfer {{path/to/repo.git}} download`
