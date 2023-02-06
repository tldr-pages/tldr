# git cvsexportcommit

> Egyetlen `Git` commit exportálása egy CVS checkoutba. További információ: <https://git-scm.com/docs/git-cvsexportcommit>.

- Egy adott javítás beolvasztása a CVS-be:

`git cvsexportcommit -v -c -w {{path/to/project_cvs_checkout}} {{commit_sha1}}`
