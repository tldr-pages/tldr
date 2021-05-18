# bfg

> Remove large files or passwords from Git history like git-filter-branch
> More information: <https://rtyley.github.io/bfg-repo-cleaner/>.

- Remove a file with sensitive data and leave the latest commit untouched:

`bfg --delete-files {{FILE-WITH-SENSITIVE-DATA}}`

- Replace all text listed in passwords.txt wherever it can be found in the repository's history:

`bfg --replace-text {{passwords.txt}}`

- After the sensitive data is removed, you must force push your changes to GitHub:

`git push --force`
