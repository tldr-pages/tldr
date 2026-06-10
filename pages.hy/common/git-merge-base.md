# git merge-base

> Գտեք երկու պարտավորությունների ընդհանուր նախահայր:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-merge-base>:.

- Տպեք երկու պարտավորությունների լավագույն ընդհանուր նախնին.:

`git merge-base {{commit_1}} {{commit_2}}`

- Տպեք երկու պարտավորությունների բոլոր լավագույն ընդհանուր նախնիները.:

`git merge-base {{[-a|--all]}} {{commit_1}} {{commit_2}}`

- Ստուգեք՝ արդյոք commit-ը կոնկրետ կոմիթի նախահայրն է.:

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
