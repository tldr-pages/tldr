# git merge-index

> Rulează un program de fuziune pe fișierele care necesită fuziune.
> Mai multe informații: <https://git-scm.com/docs/git-merge-index>.

- Fuzionează toate fișierele care necesită rezolvare folosind ajutorul standard:

`git merge-index git-merge-one-file -a`

- Fuzionează un fișier specific:

`git merge-index git-merge-one-file -- {{path/to/file}}`

- Fuzionează mai multe fișiere, continuând în caz de erori:

`git merge-index -o git-merge-one-file -- {{path/to/file1 path/to/file2 ...}}`

- Fuzionează în tăcere toate fișierele cu un program personalizat:

`git merge-index -q {{merge-program}} -a`

- Inspectează intrările de fuziune pentru un fișier folosind `cat`:

`git merge-index cat -- {{path}}`
