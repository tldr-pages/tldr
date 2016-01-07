# git svn

> Bidirectional operation between a Subversion repository and Git.

- Clone an SVN repository:

`git svn clone {{http://example.com/my_subversion_repo}} {{local_dir}}`

- Update local clone from the upstream SVN repository:

`git svn rebase`

- Commit back to SVN repository:

`git svn dcommit`
