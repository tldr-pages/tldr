# gh թողարկում

> Կառավարեք GitHub-ի թողարկումները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_release>:.

- Ցուցակեք թողարկումները GitHub-ի պահեստում՝ սահմանափակված 30 տարրով.:

`gh release {{[ls|list]}}`

- Ցուցադրել տեղեկատվություն կոնկրետ թողարկման մասին.:

`gh release view {{tag}}`

- Ստեղծեք նոր թողարկում.:

`gh release {{[new|create]}} {{tag}}`

- Ջնջել կոնկրետ թողարկում.:

`gh release delete {{tag}}`

- Ներբեռնեք ակտիվները կոնկրետ թողարկումից.:

`gh release download {{tag}}`

- Վերբեռնեք ակտիվները կոնկրետ թողարկում.:

`gh release upload {{tag}} {{path/to/file1 path/to/file2 ...}}`
