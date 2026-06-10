# git cat-ֆայլ

> Տրամադրել բովանդակության կամ տեսակի և չափի մասին տեղեկատվություն Git պահեստի օբյեկտների համար:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-cat-file>:.

- Ստացեք `HEAD`-ի [s] չափը բայթերով.:

`git cat-file -s HEAD`

- Ստացեք տրված Git օբյեկտի [t] տիպը (blob, tree, commit, tag):

`git cat-file -t {{8c442dc3}}`

- Pretty-[p]int բովանդակությունը տվյալ Git օբյեկտի հիման վրա իր տեսակի:

`git cat-file -p {{HEAD~2}}`
