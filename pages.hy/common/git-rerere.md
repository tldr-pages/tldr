# git rerere

> Միաձուլման կոնֆլիկտների համար նորից օգտագործեք ուղղումները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-rerere>:.

- Միացնել rerere-ը ամբողջ աշխարհում.:

`git config --global rerere.enabled true`

- Մոռացեք ֆայլի գրանցված բանաձեւը.:

`git rerere forget {{path/to/file}}`

- Ստուգեք գրանցված բանաձեւերի կարգավիճակը.:

`git rerere status`
