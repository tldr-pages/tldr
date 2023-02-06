# git symbolic-ref

> Hivatkozásokat tároló fájlok olvasása, módosítása vagy törlése. További információ: <https://git-scm.com/docs/git-symbolic-ref>.

- Hivatkozás tárolása név alapján:

`git symbolic-ref refs/{{name}} {{ref}}`

- Hivatkozás név szerinti tárolása, a frissítés okát tartalmazó üzenettel együtt:

`git symbolic-ref -m "{{message}}" refs/{{name}} refs/heads/{{branch_name}}`

- Hivatkozás olvasása név szerint:

`git symbolic-ref refs/{{name}}`

- Hivatkozás törlése név szerint:

`git symbolic-ref --delete refs/{{name}}`

- A szkriptek készítéséhez rejtse el a hibákat a `--quiet` és a `--short` segítségével egyszerűsítse ("refs/heads/X" "X"-ként íródik ki):

`git symbolic-ref --quiet --short refs/{{name}}`
