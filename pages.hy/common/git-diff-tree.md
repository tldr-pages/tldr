# git diff-tree

> Համեմատում է երկու ծառի օբյեկտների միջոցով հայտնաբերված բշտիկների բովանդակությունը և եղանակը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-diff-tree>:.

- Համեմատեք երկու ծառի օբյեկտներ.:

`git diff-tree {{tree-ish1}} {{tree-ish2}}`

- Ցույց տալ փոփոխությունները երկու կոնկրետ պարտավորությունների միջև.:

`git diff-tree -r {{commit1}} {{commit2}}`

- Ցուցադրել փոփոխությունները կարկատանի ձևաչափով.:

`git diff-tree {{[-p|--patch]}} {{tree-ish1}} {{tree-ish2}}`

- Ֆիլտրի փոփոխությունները որոշակի ճանապարհով.:

`git diff-tree {{tree-ish1}} {{tree-ish2}} -- {{path/to/file_or_directory}}`
