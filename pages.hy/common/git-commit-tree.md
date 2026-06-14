# git commit-tree

> Ցածր մակարդակի օգտակար կոմունալ օբյեկտներ ստեղծելու համար:.
> Տես նաև՝ `git commit`:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-commit-tree>:.

- Ստեղծեք commit օբյեկտ նշված հաղորդագրությամբ.:

`git commit-tree {{tree}} -m "{{message}}"`

- Ստեղծեք commit օբյեկտ, որը կարդում է հաղորդագրությունը ֆայլից (օգտագործեք `-` `stdin`-ի համար):

`git commit-tree {{tree}} -F {{path/to/file}}`

- Ստեղծեք GPG-ով ստորագրված commit օբյեկտ.:

`git commit-tree {{tree}} -m "{{message}}" {{[-S|--gpg-sign]}}`

- Ստեղծեք commit օբյեկտ նշված ծնող commit օբյեկտով.:

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`
