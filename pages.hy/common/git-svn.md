# git svn

> Երկկողմանի գործողություն Subversion պահեստի և Git-ի միջև:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-svn>:.

- Կլոնավորեք SVN պահեստը.:

`git svn clone {{https://example.com/subversion_repo}} {{local_directory}}`

- Կլոնավորեք SVN պահոցը՝ սկսած տվյալ վերանայման համարից.:

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_directory}}`

- Թարմացրեք տեղական կլոնը հեռավոր SVN պահոցից.:

`git svn rebase`

- Ստացեք թարմացումներ հեռավոր SVN պահոցից՝ առանց Git `HEAD` փոխելու:

`git svn fetch`

- Վերադարձեք SVN պահեստին.:

`git svn commit`
