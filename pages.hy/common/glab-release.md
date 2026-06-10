# glab թողարկում

> Կառավարեք GitLab-ի թողարկումները:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/release/_index.md>:.

- Ցուցակեք թողարկումները Gitlab-ի պահեստում՝ սահմանափակված 30 տարրով.:

`glab release list`

- Ցուցադրել տեղեկատվություն կոնկրետ թողարկման մասին.:

`glab release view {{tag}}`

- Ստեղծեք նոր թողարկում.:

`glab release create {{tag}}`

- Ջնջել կոնկրետ թողարկում.:

`glab release delete {{tag}}`

- Ներբեռնեք ակտիվները կոնկրետ թողարկումից.:

`glab release download {{tag}}`

- Վերբեռնեք ակտիվները կոնկրետ թողարկում.:

`glab release upload {{tag}} {{path/to/file1 path/to/file2 ...}}`
