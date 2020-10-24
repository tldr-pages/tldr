# git svn

> Bidirectional operation between a Subversion repository and Git.
> More information: <https://git-scm.com/docs/git-svn>.

- Clone an SVN repository:

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- Clone a SVN repository starting at a given revision number:

`git svn clone -r{{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- Update local clone from the remote SVN repository:

`git svn rebase`

- Fetch updates from the remote SVN repository without changing the git HEAD:

`git svn fetch`

- Commit back to the SVN repository:

`git svn dcommit`
