# git svn

> Bidirectional operation between a Subversion repository and Git

- clone an SVN repository

`git svn clone {{http://example.com/my_subversion_repo}} {{local_dir}}`

- update local clone from the upstream SVN repository

`git svn rebase`

- commit back to SVN repository

`git svn dcommit`
